from django import forms

from PetPalStories.stories.models import Story


class StoryDeleteForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name in self.fields:
    #
    #         self.fields[field_name].widget.attrs['readonly'] = 'readonly'
    #         self.fields[field_name].required = False


class StoryEditForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'pet_name', 'story_text', 'pet_species', 'image')