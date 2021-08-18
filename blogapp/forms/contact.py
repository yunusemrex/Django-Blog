from blogapp import forms
from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(max_length=35)
    full_name = forms.CharField(max_length=35)
    message = forms.CharField(widget=forms.Textarea)