from django.contrib import admin

from PetPalStories.common.models import FavouriteStory, MessageStory


@admin.register(FavouriteStory)
class FavouriteStoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'story', 'user')


@admin.register(MessageStory)
class MessageStoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'sender', 'receiver', 'story', 'sent_on', 'is_read')