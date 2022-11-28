from django import forms

from PetPalStories.forum.models import Post


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('published_on', 'owner', )