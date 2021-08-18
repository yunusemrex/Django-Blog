from django.shortcuts import render, redirect
from blogapp.forms import ContactForm
from blogapp.models import ContactModel


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = ContactModel()
            contact.email = form.cleaned_data['email']
            contact.full_name = form.cleaned_data['full_name']
            contact.message = form.cleaned_data['message']
            contact.save()
            return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'pages/contact.html', context=context)