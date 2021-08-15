from django.shortcuts import render
from django.http import HttpResponse


def contact(request):
    return render(request, 'pages/contact.html', context={})