from cloudinary.forms import CloudinaryFileField
from django import forms

from PetPalStories.core import validators
from PetPalStories.stories.models import Story


class StoryBaseForm(forms.ModelForm):
    image = CloudinaryFileField(
        # attrs={'style': "margin-top: 30px"},
        validators=(validators.validate_image_size,),
        options={
            'tags': "directly_uploaded",
            'crop': 'limit', 'width': 500, 'height': 500,
            'eager': [{'crop': 'fill', 'width': 150, 'height': 100}]
        },
        required=False,
        help_text=f'Please, make sure your image size is up to {validators.MAX_IMAGE_SIZE_MB}MB',
    )

    class Meta:
        model = Story
        fields = ('title', 'pet_name', 'story_text', 'pet_species', 'image')


class StoryDeleteForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ()


class StoryCreateForm(StoryBaseForm):
    ...


class StoryEditForm(StoryBaseForm):
    ...