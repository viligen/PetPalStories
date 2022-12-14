from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

from PetPalStories.petitions.models import Petition
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
        on_delete=models.CASCADE,
        null=True,
        blank=True,

    )
    sender = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='sender'


    )
    receiver = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
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
        verbose_name_plural = 'Message Stories'


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

    class Meta:
        verbose_name_plural = 'Favourite Stories'


class SignedPetition(models.Model):
    petition = models.ForeignKey(
        to=Petition,
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
    signed_on = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )
    is_agreed = models.BooleanField(

        verbose_name='Personal data terms and conditions: '

    )

    class Meta:
        unique_together = ('user', 'petition',)
        ordering = ('-signed_on',)