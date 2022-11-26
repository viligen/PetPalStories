from django.contrib import admin

from PetPalStories.stories.models import Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'pet_name', 'pet_species', 'owner', 'image',)
    list_filter = ('id', 'pet_species', 'owner', 'slug')
    search_fields = ('slug__startswith', 'slug__endswith', 'pet_name', 'pet_species', 'owner__username')
    ordering = ('id', 'slug', 'pet_name', 'pet_species', 'owner',)