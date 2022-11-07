from django.urls import path

from PetPalStories.common.views import index_view

urlpatterns = [
    path('', index_view, name='index'),

]