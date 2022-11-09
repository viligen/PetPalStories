from django.urls import path

from PetPalStories.stories.views import StoriesListView, AddStoryView

urlpatterns = [

    path('', StoriesListView.as_view(), name='stories'),
    path('add/', AddStoryView.as_view(), name='add story'),
    path('details/<slug:slug>/', AddStoryView.as_view(), name='details story'),
    path('edit/<slug:slug>/', AddStoryView.as_view(), name='edit story'),
    path('delete/<slug:slug>/', AddStoryView.as_view(), name='delete story'),
]