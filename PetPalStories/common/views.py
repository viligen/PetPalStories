from django.shortcuts import render, redirect
from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.urls import reverse_lazy
from django.views import generic

from PetPalStories.common.forms import MessageStoryForm
from PetPalStories.common.models import MessageStory
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
        story_slug = Story.objects.filter(slug=self.kwargs['slug']).get().slug
        return reverse_lazy('details story', kwargs={'slug': story_slug})

    def form_valid(self, form):
        form.instance.sender_id = self.request.user.pk
        form.instance.story_id = Story.objects.filter(slug=self.kwargs['slug']).get().pk
        form.instance.receiver_id = Story.objects.filter(slug=self.kwargs['slug']).get().owner_id

        return super().form_valid(form)


class MessageListView(generic.ListView):
    model = MessageStory
    template_name = 'accounts/user-messages.html'
    context_object_name = 'messages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['new_messages'] = MessageStory.objects.filter(receiver=self.request.user.pk, is_read=False)
        context['read_messages'] = MessageStory.objects.filter(receiver=self.request.user.pk, is_read=True)
        context['sent_messages'] = MessageStory.objects.filter(sender=self.request.user.pk)
        return context


def mark_as_read(request, pk_message, pk):

    message = MessageStory.objects.filter(pk=pk_message).get()
    message.is_read = True
    message.save()
    return redirect('messages user', pk=pk)


def delete_message(request, pk_message, pk):
    message = MessageStory.objects.filter(pk=pk_message).get()
    message.delete()

    return redirect('messages user', pk=pk)