import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.urls import reverse_lazy
from django.views import generic

from PetPalStories.common.forms import MessageStoryForm, SignedPetitionForm
from PetPalStories.common.models import MessageStory, FavouriteStory, SignedPetition
from PetPalStories.core.my_Mixins import OwnerRequiredMixin
from PetPalStories.petitions.models import Petition
from PetPalStories.stories.models import Story

UserModel = get_user_model()


def index_view(request):

    if request.user.is_authenticated:
        return redirect('stories')
    return render(request, 'common/index.html')


class MessageStoryCreateView(auth_mixins.LoginRequiredMixin, generic.CreateView):
    model = MessageStory
    form_class = MessageStoryForm
    template_name = 'common/story-message.html'
    context_object_name = 'message'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        story = Story.objects.filter(slug=self.kwargs['slug']).get()
        context['sender'] = self.request.user.username
        context['receiver'] = UserModel.objects.filter(pk=story.owner_id).get().username
        context['story'] = story
        return context

    def get_success_url(self):
        messages.success(self.request, 'Message was successfully sent')
        return reverse_lazy('messages user', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        form.instance.sender_id = self.request.user.pk
        form.instance.story_id = Story.objects.filter(slug=self.kwargs['slug']).get().pk
        form.instance.receiver_id = Story.objects.filter(slug=self.kwargs['slug']).get().owner_id

        return super().form_valid(form)


class MessageListView(OwnerRequiredMixin, generic.ListView):
    model = MessageStory
    template_name = 'common/user-my-messages.html'
    context_object_name = 'my_messages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        received_msgs = MessageStory.objects.filter(receiver=self.request.user.pk)
        context['new_messages'] = received_msgs.filter(is_read=False)
        context['read_messages'] = received_msgs.filter(is_read=True)
        context['sent_messages'] = MessageStory.objects.filter(sender=self.request.user.pk)
        return context


@login_required()
def mark_as_read(request, pk_message, pk):

    message = MessageStory.objects.filter(pk=pk_message).get()
    message.is_read = True
    message.seen_on = datetime.datetime.now()
    message.save()
    return redirect('messages user', pk=pk)


@login_required()
def delete_message(request, pk_message, pk):
    message = MessageStory.objects.filter(pk=pk_message).get()
    message.delete()
    messages.warning(request, 'Message was successfully deleted')
    return redirect('messages user', pk=pk)


@login_required()
def favourite_story(request, slug):
    story = Story.objects.filter(slug=slug).get()
    fav_story = FavouriteStory.objects.filter(story_id=story.pk, user_id=request.user.pk) or None

    if fav_story is not None:
        fav_story.get().delete()
        messages.warning(request, 'Story was successfully removed from Favourites')
        return redirect('details story', slug=slug)
    fav_story = FavouriteStory(user=request.user, story=story)
    fav_story.save()
    messages.success(request, 'Story was successfully added to Favourites')
    return redirect('details story', slug=slug)


class MyFavouriteStories(OwnerRequiredMixin, generic.ListView):
    model = FavouriteStory
    template_name = 'common/user-my-favourite-stories.html'
    context_object_name = 'stories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stories_fav = FavouriteStory.objects.filter(user_id=self.request.user.pk)
        context['stories_filtered'] = [Story.objects.filter(pk=s.story_id).get() for s in stories_fav]
        last_seen_query = [Story.objects.filter(pk=pk).get() for pk in set(self.request.session.get('last_seen', []))][:5]
        context['last_seen'] = last_seen_query
        return context


class MyPublishedStories(OwnerRequiredMixin, generic.ListView):
    model = Story
    template_name = 'common/user-my-own-stories.html'
    context_object_name = 'stories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['stories_filtered'] = Story.objects.filter(owner_id=self.request.user.pk)
        return context


class MyOwnPetitions(OwnerRequiredMixin, generic.ListView):
    model = Petition
    template_name = 'common/user-my-own-petitions.html'
    context_object_name = 'petitions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        own_petitions = Petition.objects.filter(owner_id=self.request.user.pk)
        context['my_petitions'] = own_petitions.filter(is_active=True)
        context['my_petitions_stopped'] = own_petitions.filter(is_active=False)
        return context


class SignPetitionCreateView(auth_mixins.LoginRequiredMixin, generic.CreateView):
    model = SignedPetition
    form_class = SignedPetitionForm
    template_name = 'common/sign-petition.html'
    context_object_name = 'singed_petition'

    def dispatch(self, request, *args, **kwargs):
        user = UserModel.objects.filter(pk=self.request.user.pk).get()
        if not user.first_name or not user.last_name:
            messages.warning(request, 'You need to update your account details with first and/or last name'
                                        ' in order to be able to sign a Petition off')
            return redirect('edit user', pk=user.pk)

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        petition = Petition.objects.filter(slug=self.kwargs['slug']).get()

        context['petition'] = petition
        return context

    def get_success_url(self):
        messages.success(self.request, 'Petition was successfully signed')
        return reverse_lazy('details petition', kwargs={'slug': self.kwargs['slug']})

    def form_valid(self, form):
        form.instance.user_id = self.request.user.pk

        form.instance.petition_id = Petition.objects.filter(slug=self.kwargs['slug']).get().pk

        return super().form_valid(form)