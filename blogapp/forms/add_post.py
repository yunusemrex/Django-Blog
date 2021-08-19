from django import forms
from blogapp.models import PostModel


class AddPostModelForm(forms.ModelForm):
    class Meta : 
        model = PostModel
        exclude = ('author','slug')
