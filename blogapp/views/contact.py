from django.shortcuts import render, redirect
from blogapp.forms import ContactForm
from blogapp.models import ContactModel
from django.views.generic import FormView


class ContactFormView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = '/contact/email-sent'


    def form_valid(self, form):
        form.save()
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