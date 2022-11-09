from django.contrib import admin

from PetPalStories.stories.models import Story


# Register your models here.
@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    pass