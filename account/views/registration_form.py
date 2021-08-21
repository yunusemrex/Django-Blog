from django.shortcuts import redirect, render
from django.contrib import messages
from account.forms import RegistrationForm
from django.contrib.auth import login, authenticate

def registration_form(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form =  RegistrationForm()
    return render(request, 'pages/register.html', context={
        'form':form

    })