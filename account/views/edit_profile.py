from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import ProfilEditForm

@login_required(login_url='/')
def edit_profile(request):
    if request.method == "POST":
        form =  ProfilEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated.')
    else:
        form = ProfilEditForm(instance = request.user)
    return render(request, 'pages/edit-profile.html', context={
        'form':form

    })