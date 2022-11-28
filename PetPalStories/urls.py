"""PetPalStories URL Configuration

"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from PetPalStories import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('PetPalStories.common.urls')),
    path('accounts/', include('PetPalStories.accounts.urls')),
    path('stories/', include('PetPalStories.stories.urls')),
    path('petitions/', include('PetPalStories.petitions.urls')),
    path('forum/', include('PetPalStories.forum.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)