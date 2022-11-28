from django.urls import path

from PetPalStories.forum.views import PostsListView, PostAddView

urlpatterns = [
        path('', PostsListView.as_view(), name='forum dashboard'),
        path('add/', PostAddView.as_view(), name='add post'),
        # path('api/comments/?<int:post_pk>/', name='post comments'),
        # path('api/comments/add/<int:post_pk>/', name='add post comment'),
]