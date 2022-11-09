from django.contrib.auth import mixins as auth_mixins

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from PetPalStories.stories.models import Story


# Create your views here.
class StoriesListView(generic.ListView):
    model = Story
    template_name = 'stories/stories-dashboard.html'
    context_object_name = 'stories'


class AddStoryView(auth_mixins.LoginRequiredMixin, generic.CreateView):
    model = Story
    fields = '__all__'
    template_name = 'stories/story-add.html'
    success_url = reverse_lazy('stories')