from django.contrib import admin

from PetPalStories.petitions.models import Petition


@admin.register(Petition)
class PetitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'location', 'goal', 'image', 'owner',)
    list_filter = ('id', 'location', 'owner', 'slug')
    search_fields = ('slug__startswith', 'slug__endswith', 'location', 'goal', 'owner__username')