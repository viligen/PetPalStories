from django import forms
from django.contrib.auth import get_user_model

from PetPalStories.common.models import MessageStory, SignedPetition

UserModel = get_user_model()


class MessageStoryForm(forms.ModelForm):
    class Meta:
        model = MessageStory
        fields = ('text',)
        labels = {
            'text': ''
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['placeholder'] = 'Type your message here...'


class SignedPetitionForm(forms.ModelForm):
    class Meta:
        model = SignedPetition
        fields = ('is_agreed',)
        help_texts = {
            'is_agreed': 'Your personal data will be passed to Petition Signatures Data Base. '
                         'Please, check this field to agree'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_agreed'].required = True