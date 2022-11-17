from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from PetPalStories.core.validators import validate_image_size

UserModel = get_user_model()


class Story(models.Model):
    SPECIES = ['Dog', 'Cat', 'Bird', 'Rabbit', 'Fish', 'Lizard', 'Snake', 'Other']
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

    story_text = models.TextField(
        validators=(
            MinLengthValidator(MIN_LEN_TEXT, message=ERROR_MESSAGE_TEXT_FIELD),
        ),
        verbose_name="Pet's story"
    )
    image = models.ImageField(
        upload_to='stories_images/',

        validators=(
            validate_image_size,
        ),
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
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    owner = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,

        null=False,
        blank=True,

    )

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.id}')

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Stories'
        unique_together = ('title', 'id')
        ordering = ('-published_on', )