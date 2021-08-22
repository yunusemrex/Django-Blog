from django import forms
from blogapp.models import ContactModel
from django.core.mail import send_mail

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('full_name','email', 'message')

    def send_email(self, message):
        send_mail(
            subject='İletişim Formundan Yeni Mesaj Var!',
            message=message,
            from_email=None,
            recipient_list=['backendwithdjango@gmail.com'],
            fail_silently=False
        )