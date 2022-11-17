from django.contrib.auth import get_user_model
from django.db import models

from PetPalStories.stories.models import Story

UserModel = get_user_model()


class MessageStory(models.Model):
    text = models.TextField(

    )

    sent_on = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True
    )
    seen_on = models.DateTimeField(
        default=None,
        null=True,
        blank=True
    )

    is_read = models.BooleanField(
        default=False,
        blank=True,
    )

    story = models.ForeignKey(
        to=Story,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,

    )
    sender = models.ForeignKey(
        to=UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sender'


    )
    receiver = models.ForeignKey(
        to=UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='receiver'
    )

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
        if not self.receiver:
            self.receiver = Story.objects.filter(pk=self.story_id).get().owner

        return super().save(*args, **kwargs)
    @property
    def subject(self):
        story = Story.objects.filter(pk=self.story_id).get()
        return story.title

    class Meta:
        ordering = ('-sent_on',)


class FavouriteStory(models.Model):
    story = models.ForeignKey(
        to=Story,
        on_delete=models.CASCADE,
        null=True,
        blank=True,

    )
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,

    )