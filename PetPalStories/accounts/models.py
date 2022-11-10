from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from PetPalStories.core.validators import validate_only_letters


class AppUser(auth_models.AbstractUser):

    MIN_LEN_FN = 2
    MAX_LEN_FN = 30

    MIN_LEN_LN = 2
    MAX_LEN_LN = 30

    GENDERS = ['Male', 'Female', 'I prefer not to say']
    CHOICES = [(c, c) for c in GENDERS]

    email = models.EmailField(
        unique=True,

    )

    first_name = models.CharField(
        max_length=MAX_LEN_FN,
        validators=(
            MinLengthValidator(MIN_LEN_FN),
            validate_only_letters,
        ),
        null=True,
        blank=True,
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LN,
        validators=(
            MinLengthValidator(MIN_LEN_LN),
            validate_only_letters,
        ),
        null=True,
        blank=True,
        verbose_name='Last Name'
    )
    gender = models.CharField(
        max_length=max(len(g) for g in GENDERS),
        choices=CHOICES,
        default='I prefer not to say',
        null=False,
        blank=True,
    )

    # USERNAME_FIELD = 'email'