from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic

from PetPalStories.petitions.forms import PetitionCreateForm
from PetPalStories.petitions.models import Petition


class PetitionsListView(generic.ListView):
    PAGE_SIZE = 4
    model = Petition
    template_name = 'petitions/petitions-dashboard.html'
    context_object_name = 'petitions'

    paginate_by = PAGE_SIZE

    def get_queryset(self):
        query = self.request.GET.get('query', '').strip()

        object_list = self.model.objects.all()
        if query:
            object_list = object_list\
                .filter(Q(location__icontains=query) | Q(title__icontains=query))
        return object_list


class PetitionAddView(auth_mixins.LoginRequiredMixin, generic.CreateView):
    model = Petition
    form_class = PetitionCreateForm
    template_name = 'petitions/petition-add.html'
    success_url = reverse_lazy('petitions')

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.pk
        return super().form_valid(form)