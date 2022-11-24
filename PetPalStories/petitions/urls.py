from django.urls import path

from PetPalStories.petitions.views import PetitionAddView, PetitionsListView, PetitionEditView, PetitionDetailsView, \
    PetitionStopView

urlpatterns = [

    path('', PetitionsListView.as_view(), name='petitions'),
    path('add/', PetitionAddView.as_view(), name='add petition'),
    path('details/<slug:slug>/', PetitionDetailsView.as_view(), name='details petition'),
    path('edit/<slug:slug>/<int:pk>/', PetitionEditView.as_view(), name='edit petition'),
    path('stop/<slug:slug>/<int:pk>/', PetitionStopView.as_view(), name='stop petition'),

]