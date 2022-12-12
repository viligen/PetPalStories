from django import template

from PetPalStories.common.models import FavouriteStory

register = template.Library()


@register.filter(name='is_favourite')
def is_favourite(story, user):
    return FavouriteStory.objects.filter(story=story, user=user).count() > 0