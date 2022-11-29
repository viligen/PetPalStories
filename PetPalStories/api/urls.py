from django.urls import path

from PetPalStories.api.views import CommentsListApiView, CommentCreateView

urlpatterns = [
    path('comments/add/', CommentCreateView.as_view(), name='add post comment'),
    path('comments/?', CommentsListApiView.as_view(), name='post comments'),

]