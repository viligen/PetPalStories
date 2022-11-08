from django.shortcuts import render
from django.views import generic

from PetPalStories.stories.models import Story


# Create your views here.
class StoriesView(generic.ListView):
    model = Story
    template_name = 'stories/stories-dashboard.html'
    context_object_name = 'stories'