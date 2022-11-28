from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

UserModel = get_user_model()


class Post(models.Model):
    MIN_LEN_TOPIC = 10
    ERROR_MESSAGE_TOPIC = f'You are supposed to enter at least {MIN_LEN_TOPIC} characters'

    topic = models.TextField(
       validators=(MinLengthValidator(MIN_LEN_TOPIC, message=ERROR_MESSAGE_TOPIC), )
    )

    published_on = models.DateTimeField(
        auto_now_add=True,

    )

    owner = models.ForeignKey(
        to=UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ('-published_on',)


class Comment(models.Model):
    text = models.TextField(

    )
    published_on = models.DateTimeField(
        auto_now_add=True,

    )

    owner = models.ForeignKey(
        to=UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    post_parent = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    class Meta:
        ordering = ('published_on',)