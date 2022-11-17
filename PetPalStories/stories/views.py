from django.contrib.auth import mixins as auth_mixins


from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from PetPalStories.common.models import FavouriteStory
from PetPalStories.stories.models import Story


class StoriesListView(generic.ListView):
    model = Story
    template_name = 'stories/stories-dashboard.html'
    context_object_name = 'stories'


class AddStoryView(auth_mixins.LoginRequiredMixin, generic.CreateView):
    model = Story
    fields = ('title', 'pet_name', 'story_text', 'pet_species', 'image')
    template_name = 'stories/story-add.html'
    success_url = reverse_lazy('stories')

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.pk
        return super().form_valid(form)


class StoryDetailsView(auth_mixins.LoginRequiredMixin, generic.DetailView):
    model = Story
    template_name = 'stories/story-details.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_favourite'] = FavouriteStory.objects.filter(user=self.request.user, story=self.object) or None

        return context