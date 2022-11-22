from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic

from PetPalStories.petitions.forms import PetitionCreateForm, PetitionEditForm, PetitionStopForm
from PetPalStories.petitions.models import Petition


class PetitionsListView(generic.ListView):
    PAGE_SIZE = 3
    model = Petition
    template_name = 'petitions/petitions-dashboard.html'
    context_object_name = 'petitions'

    paginate_by = PAGE_SIZE

    def get_queryset(self):
        query = self.request.GET.get('query', '').strip()

        object_list = self.model.objects.filter(is_active=True)
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


class PetitionEditView(auth_mixins.LoginRequiredMixin, generic.UpdateView):
    model = Petition
    template_name = 'petitions/petition-edit.html'
    context_object_name = 'petition'
    form_class = PetitionEditForm

    def get_success_url(self):
        return reverse_lazy('details petition', kwargs={'slug': self.kwargs['slug']})


class PetitionDetailsView(auth_mixins.LoginRequiredMixin, generic.DetailView):
    model = Petition
    template_name = 'petitions/petition-details.html'
    context_object_name = 'petition'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: when sign feature
        context['is_signed'] = False
        context['last_signed_on'] = 0
        context['last_signed_from'] = 'someone'
        total_signatures = 0
        context['still_to_go'] = self.object.goal - total_signatures
        return context


class PetitionStopView(auth_mixins.LoginRequiredMixin, generic.UpdateView):
    model = Petition
    template_name = 'petitions/petition-stop.html'
    context_object_name = 'petition'
    form_class = PetitionStopForm
    success_url = reverse_lazy('petitions')

    def form_valid(self, form):
        form.instance.is_active = False
        return super().form_valid(form)