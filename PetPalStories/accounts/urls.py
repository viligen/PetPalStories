
from django.urls import path, include

from PetPalStories.accounts.views import SignInView, SignUpView, SignOutView, ProfileDetailsView, ProfileEditView, ProfileDeleteView
from PetPalStories.common.views import MessageListView, mark_as_read, delete_message

urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='details user'),
        path('edit/', ProfileEditView.as_view(), name='edit user'),
        path('delete/', ProfileDeleteView.as_view(), name='delete user'),
        path('messages/', MessageListView.as_view(), name='messages user'),
        path('messages/<int:pk_message>/', mark_as_read, name='mark as read messages'),
        path('messages/delete/<int:pk_message>/', delete_message, name='delete messages'),


    ]))
]