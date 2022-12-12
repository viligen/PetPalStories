from django import template

from PetPalStories.common.models import MessageStory

register = template.Library()


@register.simple_tag(name='filter_new_msgs')
def filter_new_msgs(user):
    return MessageStory.objects.filter(receiver=user, is_read=False).count()