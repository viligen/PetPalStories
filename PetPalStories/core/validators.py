
from django.core.exceptions import ValidationError


MAX_IMAGE_SIZE_MB = 1.0
MAX_IMAGE_SIZE_B = MAX_IMAGE_SIZE_MB * 1024 * 1024
ERROR_MESSAGE_IMAGE_SIZE = f"Your picture's size should not exceed {MAX_IMAGE_SIZE_MB}MB"

ERROR_MESSAGE_NOT_CHARS = 'You need to use alphabetic characters only'


def validate_image_size(file_obj):
    print(file_obj)
    filesize = file_obj.metadata['bytes']

    if filesize > MAX_IMAGE_SIZE_B:
        raise ValidationError(message=ERROR_MESSAGE_IMAGE_SIZE)


def validate_only_letters(value):
    if value and not all([ch.isalpha() for ch in value]):
        raise ValidationError(message=ERROR_MESSAGE_NOT_CHARS)