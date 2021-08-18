from django.shortcuts import render, redirect
from blogapp.forms import ContactForm
from blogapp.models import ContactModel


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'pages/contact.html', context=context)