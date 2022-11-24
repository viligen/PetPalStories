from django.urls import path, include

from PetPalStories.common.views import index_view, MessageListView, mark_as_read, delete_message, \
    MessageStoryCreateView, favourite_story, MyFavouriteStories, MyPublishedStories, MyOwnPetitions, \
    SignPetitionCreateView

urlpatterns = [
    path('', index_view, name='index'),

    path('profile/<int:pk>/mymessages/', include([
        path('', MessageListView.as_view(), name='messages user'),
        path('<int:pk_message>/', mark_as_read, name='mark as read messages'),
        path('delete/<int:pk_message>/', delete_message, name='delete messages')])),

    path('profile/<int:pk>/', include([
        path('myfavouritestories/', MyFavouriteStories.as_view(), name='favourite stories user'),
        path('myownstories/', MyPublishedStories.as_view(), name='own published stories user'),
        path('myownpetitions/', MyOwnPetitions.as_view(), name='own petitions user'),
    ])),

    path('stories/<slug:slug>/', include([
        path('message/', MessageStoryCreateView.as_view(), name='message story'),
        path('favourite/', favourite_story, name='favourite story'), ])),

    path('petitions/<slug:slug>/sign/<int:pk>/', SignPetitionCreateView.as_view(), name='sign petition'),


]