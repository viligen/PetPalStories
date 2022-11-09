from django.core.exceptions import ValidationError

MAX_IMAGE_SIZE_MB = 5.0
MAX_IMAGE_SIZE_B = MAX_IMAGE_SIZE_MB * 1024 * 1024
ERROR_MESSAGE_IMAGE_SIZE = f"Your picture's size should not exceed {MAX_IMAGE_SIZE_MB}MB"


def validate_image_size(file_obj):

    filesize = file_obj.file.size

    if filesize > MAX_IMAGE_SIZE_B:
        raise ValidationError(message=ERROR_MESSAGE_IMAGE_SIZE)