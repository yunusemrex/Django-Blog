from django.core import paginator
from django.shortcuts import render
from blogapp.models import PostModel
from django.core.paginator import Paginator

def index(request):
    posts = PostModel.objects.order_by('-id')
    page = request.GET.get('page')

    paginator = Paginator(posts, 2)

    return render(request, 'pages/index.html', context={
        'posts': paginator.get_page(page)
    })