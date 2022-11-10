from django.urls import path

from PetPalStories.accounts.views import SignInView, ProfileView, SignUpView

urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='details user'),
]