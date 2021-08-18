from django.forms.widgets import TextInput
from blogapp import forms
from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(label='E-mail', max_length=35)
    full_name = forms.CharField(label='Full name', max_length=35)
    message = forms.CharField(widget=forms.Textarea())