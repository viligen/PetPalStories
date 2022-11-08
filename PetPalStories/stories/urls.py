from django.urls import path

from PetPalStories.stories.views import StoriesView

urlpatterns = [

    path('', StoriesView.as_view(), name='stories')
]