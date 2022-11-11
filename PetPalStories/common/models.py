from django.contrib.auth import get_user_model
from django.db import models

from PetPalStories.stories.models import Story

UserModel = get_user_model()


class Message(models.Model):
    text = models.TextField(

    )

    sent_on = models.DateTimeField(
        auto_now_add=True,
        null=False,
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
    owner = models.ForeignKey(
        to=UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,

    )


class Favourite(models.Model):
    story = models.ForeignKey(
        to=Story,
        on_delete=models.CASCADE,
        null=True,
        blank=True,

    )
    owner = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,

    )