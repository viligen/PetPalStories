from django.contrib.auth import views as auth_views, get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/user-login.html'


class SignUpView(generic.CreateView):
    model = UserModel
    template_name = 'accounts/user-register.html'
    fields = ('username', 'password')


class ProfileView(generic.DetailView):
    pass