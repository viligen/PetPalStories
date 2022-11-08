from django.core.validators import MinLengthValidator
from django.db import models

from PetPalStories.core.validators import validate_image_size


# Create your models here.


class Story(models.Model):
    SPECIES = ['Dog', 'Cat', 'Bird', 'Fish', 'Lizard', 'Snake', 'Other']
    CHOICES = [(c, c) for c in SPECIES]

    MAX_LEN_TITLE = 50
    MAX_LEN_PET = 20
    MIN_LEN_TEXT = 10

    ERROR_MESSAGE_TEXT_FIELD = f'You are supposed to enter at least {MIN_LEN_TEXT} characters'

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        unique=True,
    )
    pet_name = models.CharField(
        max_length=MAX_LEN_PET,
        verbose_name='Pet Name'
    )

    text = models.TextField(
        validators=(
            MinLengthValidator(MIN_LEN_TEXT, message=ERROR_MESSAGE_TEXT_FIELD),
        )
    )
    picture = models.ImageField(
        upload_to='pet_photos/',

        validators=(
            validate_image_size,
        ),
        default='Pet Image',
        null=True,
        blank=True,
    )

    pet_species = models.CharField(
        max_length=max(len(c) for c in SPECIES),
        choices=CHOICES,
        default='Other',
        null=True,
        blank=True,
        verbose_name='Pet Species'
    )

    published_on = models.DateTimeField(
        auto_now_add=True,
    )
    edited_on = models.DateTimeField(
        auto_now=True,
    )
    # owner = models.ForeignKey(
    #     to=User,
    #     on_delete=models.CASCADE,
    #     default=None,
    #     null=True,
    #     blank=True,
    #
    # )