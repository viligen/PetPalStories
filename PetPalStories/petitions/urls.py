from django.urls import path

from PetPalStories.petitions.views import PetitionAddView, PetitionsListView

urlpatterns = [

    path('', PetitionsListView.as_view(), name='petitions'),
    path('add/', PetitionAddView.as_view(), name='add petition'),
    path('details/<slug:slug>/', PetitionAddView.as_view(), name='details petition'),
    path('edit/<slug:slug>/', PetitionAddView.as_view(), name='edit petition'),
    path('stop/<slug:slug>/', PetitionAddView.as_view(), name='stop petition'),

]