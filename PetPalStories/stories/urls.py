from django.urls import path


from PetPalStories.stories.views import StoriesListView, StoryAddView, StoryDetailsView, StoryDeleteView, StoryEditView

urlpatterns = [

    path('', StoriesListView.as_view(), name='stories'),
    path('add/', StoryAddView.as_view(), name='add story'),
    path('details/<slug:slug>/', StoryDetailsView.as_view(), name='details story'),
    path('edit/<slug:slug>/<int:pk>/', StoryEditView.as_view(), name='edit story'),
    path('delete/<slug:slug>/<int:pk>/', StoryDeleteView.as_view(), name='delete story'),

]