from django.urls import path

from PetPalStories.forum.views import PostsListView, PostAddView

urlpatterns = [
        path('', PostsListView.as_view(), name='forum dashboard'),
        path('add/', PostAddView.as_view(), name='add post'),

]