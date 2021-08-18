from django import forms
from django import forms
from blogapp.models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('email','full_name','message')