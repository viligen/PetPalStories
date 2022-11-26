from django.contrib import messages
from django.contrib.auth import views as auth_views, get_user_model, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from PetPalStories.accounts.forms import UserCreateForm
from PetPalStories.common.models import FavouriteStory
from PetPalStories.core.my_Mixins import OwnerRequiredMixin
from PetPalStories.petitions.models import Petition
from PetPalStories.stories.models import Story

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/user-login.html'
    # next_page = 'stories'


class SignUpView(generic.CreateView):

    template_name = 'accounts/user-register.html'
    form_class = UserCreateForm

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        new_user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'],
                                email=form.cleaned_data['email']
                                )
        login(self.request, new_user)
        messages.success(self.request, 'Your registration was successful, you are now logged in')
        return redirect(self.success_url)


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class ProfileDetailsView(OwnerRequiredMixin, generic.DetailView):

    model = UserModel
    template_name = 'accounts/user-details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['own_stories_count'] = Story.objects.filter(owner_id=self.request.user.pk).count()
        context['favourite_stories_count'] = FavouriteStory.objects.filter(user_id=self.request.user.pk).count()
        context['own_petitions_count'] = Petition.objects.filter(owner_id=self.request.user.pk, is_active=True).count()
        return context


class ProfileEditView(OwnerRequiredMixin, generic.UpdateView):
    model = UserModel
    template_name = 'accounts/user-edit.html'
    context_object_name = 'profile'
    fields = ('first_name', 'last_name', 'username', 'email', 'gender',)

    def get_success_url(self):
        messages.success(self.request, 'Profile  was successfully edited')
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk
        })


class ProfileDeleteView(OwnerRequiredMixin, generic.DeleteView):
    model = UserModel
    template_name = 'accounts/user-delete.html'
    success_url = reverse_lazy('index')


class ProfileChangePasswordView(OwnerRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'accounts/user-change-password.html'

    def get_success_url(self):
        messages.success(self.request, 'Password changed successfully')
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk
        })