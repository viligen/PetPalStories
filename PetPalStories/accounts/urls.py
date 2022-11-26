
from django.urls import path, include

from PetPalStories.accounts.views import SignInView, SignUpView, SignOutView, ProfileDetailsView, ProfileEditView, \
    ProfileDeleteView, ProfileChangePasswordView

urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='details user'),
        path('edit/', ProfileEditView.as_view(), name='edit user'),
        path('delete/', ProfileDeleteView.as_view(), name='delete user'),
        path('change-password/', ProfileChangePasswordView.as_view(), name='change password user')

    ]))
]