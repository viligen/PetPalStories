from django.contrib.auth import mixins as auth_mixins


from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from PetPalStories.stories.models import Story

from django.db.models.signals import pre_save
from django.dispatch import receiver


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


class StoryDetailsView(generic.DetailView):
    model = Story
    template_name = 'stories/story-details.html'
    context_object_name = 'story'