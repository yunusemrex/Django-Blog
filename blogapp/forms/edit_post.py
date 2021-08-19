from django import forms
from blogapp.models import PostModel


class EditsPostModelForm(forms.ModelForm):
    class Meta : 
        model = PostModel
        exclude = ('author','slug')
