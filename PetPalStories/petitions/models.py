from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify

from PetPalStories.core.validators import validate_image_size

from cloudinary.models import CloudinaryField

UserModel = get_user_model()


class Petition(models.Model):
    LOCATION_TARGET = ['Local', 'National', 'Europe', 'Worldwide']
    CHOICES = [(c, c) for c in LOCATION_TARGET]

    MAX_LEN_TITLE = 50
    MIN_LEN_TEXT = 10

    MIN_GOAL = 10
    ERROR_MESSAGE_GOAL = f'You are supposed to set your goal to minimum of {MIN_GOAL} signatures'

    ERROR_MESSAGE_TEXT_FIELD = f'You are supposed to enter at least {MIN_LEN_TEXT} characters'

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        unique=True,
    )

    description = models.TextField(
        validators=(
            MinLengthValidator(MIN_LEN_TEXT, message=ERROR_MESSAGE_TEXT_FIELD),
        ),
    )

    location = models.CharField(
        max_length=max(len(c) for c in LOCATION_TARGET),
        choices=CHOICES,
        default='Local',
        null=False,
        blank=True,

    )
    goal = models.PositiveIntegerField(
        validators=(
            MinValueValidator(MIN_GOAL, message=ERROR_MESSAGE_GOAL),
        )
    )

    image = CloudinaryField('image', null=True, blank=True,)

    published_on = models.DateTimeField(
        auto_now_add=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=True,
    )

    owner = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,

        null=True,
        blank=True,

    )

    @property
    def theme(self):
        return 'Pets'

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.id}')

        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.slug}'

    class Meta:

        unique_together = ('title', 'id')
        ordering = ('-published_on', )