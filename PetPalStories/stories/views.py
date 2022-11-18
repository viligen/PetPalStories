from django.contrib.auth import mixins as auth_mixins
from django.db.models import Q

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from PetPalStories.common.models import FavouriteStory
from PetPalStories.stories.forms import StoryDeleteForm, StoryEditForm
from PetPalStories.stories.models import Story


class StoriesListView(generic.ListView):
    PAGE_SIZE = 4
    model = Story
    template_name = 'stories/stories-dashboard.html'
    context_object_name = 'stories'

    paginate_by = PAGE_SIZE

    def get_queryset(self):
        pet_type_name = self.request.GET.get('query', '').strip()

        object_list = self.model.objects.all()
        if pet_type_name:
            object_list = object_list\
                .filter(Q(pet_species__icontains=pet_type_name) | Q(pet_name__icontains=pet_type_name))
        return object_list


class StoryAddView(auth_mixins.LoginRequiredMixin, generic.CreateView):
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


class StoryEditView(auth_mixins.LoginRequiredMixin, generic.UpdateView):
    model = Story
    template_name = 'stories/story-edit.html'
    context_object_name = 'story'
    form_class = StoryEditForm

    def get_success_url(self):
        return reverse_lazy('details story', kwargs={'slug': self.kwargs['slug']})


class StoryDeleteView(auth_mixins.LoginRequiredMixin, generic.DeleteView):
    model = Story
    template_name = 'stories/story-delete.html'
    context_object_name = 'story'
    form_class = StoryDeleteForm
    success_url = reverse_lazy('stories')