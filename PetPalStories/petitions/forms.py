from cloudinary.forms import CloudinaryFileField
from django import forms

from PetPalStories.core import validators
from PetPalStories.petitions.models import Petition


class PetitionBaseForm(forms.ModelForm):
    image = CloudinaryFileField(
        # attrs={'style': "margin-top: 30px"},
        validators=(validators.validate_image_size,),
        options={
            'tags': "directly_uploaded",
            'crop': 'limit', 'width': 500, 'height': 500,
            'eager': [{'crop': 'fill', 'width': 150, 'height': 100}]
        },
        required=False,

        help_text=f'Please, make sure your image size is up to {validators.MAX_IMAGE_SIZE_MB}MB'
    )

    class Meta:
        model = Petition
        exclude = ('published_on', 'slug', 'owner', 'is_active')




class PetitionCreateForm(PetitionBaseForm):
    ...


class PetitionEditForm(PetitionBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['readonly'] = 'readonly'
        self.fields['description'].widget.attrs['readonly'] = 'readonly'

        self.fields['title'].required = False
        self.fields['description'].required = False

        self.fields['title'].help_text = "You are not allowed to change petition's title"
        self.fields['description'].help_text = "You are not allowed to change petition's description"


class PetitionStopForm(PetitionBaseForm):
    class Meta:
        model = Petition
        fields = ('title', 'description',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['readonly'] = 'readonly'
            self.fields[field_name].help_text = "This field is readonly"
            self.fields[field_name].required = False