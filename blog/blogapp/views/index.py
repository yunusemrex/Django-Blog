from django.shortcuts import render
from blogapp.models import PostModel

def index(request):
    posts = PostModel.objects.all()
    return render(request, 'pages/index.html', context={
        'posts': posts
    })