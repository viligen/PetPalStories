from django.contrib import admin

from PetPalStories.common.models import FavouriteStory, MessageStory, SignedPetition


@admin.register(FavouriteStory)
class FavouriteStoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'story', 'user')
    ordering = ('id', 'story', 'user')


@admin.register(MessageStory)
class MessageStoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'sender', 'receiver', 'story', 'sent_on', 'is_read')
    ordering = ('id', 'text', 'sender', 'receiver', 'story', 'sent_on', 'is_read')


@admin.register(SignedPetition)
class SignedPetitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'petition', 'user', 'signed_on',)
    ordering = ('id', 'petition', 'user', 'signed_on',)