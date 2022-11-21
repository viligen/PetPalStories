from django import forms

from PetPalStories.petitions.models import Petition


class PetitionCreateForm(forms.ModelForm):
    class Meta:
        model = Petition
        exclude = ('published_on', 'slug', 'owner',)