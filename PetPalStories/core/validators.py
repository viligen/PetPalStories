from django.core.exceptions import ValidationError

MAX_IMAGE_SIZE = 500 * 1024
# max 500 Kb
ERROR_MESSAGE_IMAGE_SIZE = f'Your picture size should not exceed {MAX_IMAGE_SIZE/1024}Kb'


def validate_image_size(value):
    if value > MAX_IMAGE_SIZE:
        raise ValidationError(message=ERROR_MESSAGE_IMAGE_SIZE)