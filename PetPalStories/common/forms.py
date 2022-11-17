from django import forms
from django.contrib.auth import get_user_model

from PetPalStories.common.models import MessageStory

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