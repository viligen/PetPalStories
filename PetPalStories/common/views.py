import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.urls import reverse_lazy
from django.views import generic

from PetPalStories.common.forms import MessageStoryForm
from PetPalStories.common.models import MessageStory, FavouriteStory
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

        return reverse_lazy('messages user', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        form.instance.sender_id = self.request.user.pk
        form.instance.story_id = Story.objects.filter(slug=self.kwargs['slug']).get().pk
        form.instance.receiver_id = Story.objects.filter(slug=self.kwargs['slug']).get().owner_id

        return super().form_valid(form)


class MessageListView(auth_mixins.LoginRequiredMixin, generic.ListView):
    model = MessageStory
    template_name = 'common/user-my-messages.html'
    context_object_name = 'messages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['new_messages'] = MessageStory.objects.filter(receiver=self.request.user.pk, is_read=False)
        context['read_messages'] = MessageStory.objects.filter(receiver=self.request.user.pk, is_read=True)
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

    return redirect('messages user', pk=pk)


@login_required()
def favourite_story(request, slug):
    story = Story.objects.filter(slug=slug).get()
    fav_story = FavouriteStory.objects.filter(story_id=story.pk, user_id=request.user.pk) or None

    if fav_story is not None:
        fav_story.get().delete()
        return redirect('details story', slug=slug)
    fav_story = FavouriteStory(user=request.user, story=story)
    fav_story.save()
    return redirect('details story', slug=slug)


class MyFavouriteStories(auth_mixins.LoginRequiredMixin, generic.ListView):
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


class MyPublishedStories(auth_mixins.LoginRequiredMixin, generic.ListView):
    model = Story
    template_name = 'common/user-my-own-stories.html'
    context_object_name = 'stories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['stories_filtered'] = Story.objects.filter(owner_id=self.request.user.pk)
        return context