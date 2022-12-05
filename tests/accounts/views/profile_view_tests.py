from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from PetPalStories.common.models import FavouriteStory
from PetPalStories.forum.models import Post
from PetPalStories.petitions.models import Petition
from PetPalStories.stories.models import Story

UserModel = get_user_model()


def create_story_by_user(owner, count=5):
    result = []
    for i in range(count):
        story = Story(title=f'{i}+d*{i}', pet_name=f'{i+2}*i', story_text=f'{i+2}'*10, owner=owner)
        story.save()
        result.append(story)
    return result


def create_petition_by_user(owner, count=5):
    result = []
    for i in range(count):
        petition = Petition(title=f'{i}+d*{i}', description=f'{i+2}*10', goal=10, owner=owner)
        petition.save()
        result.append(petition)
    return result


def make_favourite_stories_by_user(user, stories, count=5):
    result = []
    for story in stories:
        fs = FavouriteStory(story=story, user=user)
        result.append(fs.save())

    return result


class ProfileDetailsViewTests(TestCase):
    VALID_PROFILE_DATA = {
        'username': 'testtest',
        'email': 'test33@test.bg',
        'password': '123.my4567@Q',
    }

    def _creat_user_and_login(self, user_data):
        user = UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)
        return user

    def _assert_empty_collection(self, collection_len):
        return self.assertEqual(0, collection_len, msg='Collection is not empty')

    def test_profile_details__when_is_owner__assert_True(self):
        user = self._creat_user_and_login(self.VALID_PROFILE_DATA)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertTrue(response.context['is_owner'])

    def test_profile_details__when_is_owner__assert_context_isNone_and_redirect(self):

        profile_user = self._creat_user_and_login({
            'username': 'testtestX',
            'email': 'test33@test.bgX',
            'password': '123.my4567@Q',
        })

        user = self._creat_user_and_login(self.VALID_PROFILE_DATA)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': profile_user.pk}))

        self.assertIsNone(response.context)
        self.assertEqual(response.status_code, 302)

    def test_profile__when_no_own_stories__assert_empty(self):
        user = self._creat_user_and_login(self.VALID_PROFILE_DATA)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self._assert_empty_collection(response.context['own_stories_count'])

    def test_profile__when_own_stories__assert_count_equal(self):
        user = self._creat_user_and_login(self.VALID_PROFILE_DATA)

        create_story_by_user(user, count=5)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(5, response.context['own_stories_count'])

    def test_profile__when_no_own_petitions__assert_empty(self):
        user = self._creat_user_and_login(self.VALID_PROFILE_DATA)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self._assert_empty_collection(response.context['own_petitions_count'])

    def test_profile__when_own_petitions__assert_count_equal(self):
        user = self._creat_user_and_login(self.VALID_PROFILE_DATA)

        create_petition_by_user(user, count=5)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(5, response.context['own_petitions_count'])

    def test_profile__when_no_favourites__assert_empty(self):
        user = self._creat_user_and_login(self.VALID_PROFILE_DATA)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self._assert_empty_collection(response.context['favourite_stories_count'])

    def test_profile__when_favourites__assert_count(self):
        other_user = self._creat_user_and_login({
            'username': 'testtest33',
            'email': 'test3333@test.bg',
            'password': '123.my4567@Q',
        })
        stories = create_story_by_user(other_user, count=5)

        user = self._creat_user_and_login(self.VALID_PROFILE_DATA)

        fs_list = make_favourite_stories_by_user(user, stories)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(len(fs_list), response.context['favourite_stories_count'])

    def test_profile__when_no_own_posts__assert_empty(self):
        user = self._creat_user_and_login(self.VALID_PROFILE_DATA)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self._assert_empty_collection(response.context['own_posts_count'])

    def test_profile__when_own_posts__assert_count(self):

        user = self._creat_user_and_login(self.VALID_PROFILE_DATA)

        Post.objects.create(owner=user, topic='test topic')

        expected_count = 1

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(expected_count, response.context['own_posts_count'])