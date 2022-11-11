from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from PetPalStories.accounts.forms import UserCreateForm

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/user-login.html'
    # next_page = 'stories'


class SignUpView(generic.CreateView):

    template_name = 'accounts/user-register.html'
    form_class = UserCreateForm

    success_url = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class ProfileDetailsView(LoginRequiredMixin, generic.DetailView):

    model = UserModel
    template_name = 'accounts/user-details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        return context


class ProfileEditView(LoginRequiredMixin, generic.UpdateView):
    model = UserModel
    template_name = 'accounts/user-edit.html'
    context_object_name = 'profile'
    fields = ('first_name', 'last_name', 'username', 'email', 'gender',)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk
        })


class ProfileDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = UserModel
    template_name = 'accounts/user-delete.html'
    success_url = reverse_lazy('index')