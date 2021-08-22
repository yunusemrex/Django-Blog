from django.shortcuts import render, redirect
from blogapp import forms
from blogapp.forms import ContactForm
from blogapp.models import ContactModel
from django.views.generic import FormView
from django.core.mail import message, send_mail


class ContactFormView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = '/email-sent'


    def form_valid(self, form):
        form.save()
        form.send_email(message=form.cleaned_data.get('message'))
        return super().form_valid(form)
  


# def contact(request):
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     context = {
#         'form':form
#     }
#     return render(request, 'pages/contact.html', context=context)