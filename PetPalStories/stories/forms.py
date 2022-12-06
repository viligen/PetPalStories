from cloudinary.forms import CloudinaryFileField
from django import forms

from PetPalStories.stories.models import Story


class StoryBaseForm(forms.ModelForm):
    image = CloudinaryFileField(
        # attrs={'style': "margin-top: 30px"},
        options={
            'tags': "directly_uploaded",
            'crop': 'limit', 'width': 500, 'height': 500,
            'eager': [{'crop': 'fill', 'width': 150, 'height': 100}]
        },
        required=False,)

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