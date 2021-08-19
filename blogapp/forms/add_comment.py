from django import forms
from django.forms import fields
from blogapp.models import CommentModel
from django import forms

class AddCommentModelForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('comment',)