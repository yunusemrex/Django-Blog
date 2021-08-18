from django.shortcuts import render, get_object_or_404
from blogapp.models import PostModel

def detail(request, slug):
    post = get_object_or_404(PostModel, slug=slug)
    comments = post.comments.all()
    return render(request, 'pages/detail.html', context={
        'post': post,
        'comments': comments
    })
 