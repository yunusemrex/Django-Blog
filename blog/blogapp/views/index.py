from django.core import paginator
from django.shortcuts import render
from blogapp.models import PostModel
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    query = request.GET.get('query')
    posts = PostModel.objects.order_by('-id')
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    page = request.GET.get('page')

    paginator = Paginator(posts, 2)

    return render(request, 'pages/index.html', context={
        'posts': paginator.get_page(page)
    })