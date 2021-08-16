from django.shortcuts import render
from django.http import HttpResponse


def contact(request):
    context = {
        'sayi': 5
    }
    return render(request, 'pages/contact.html', context=context)