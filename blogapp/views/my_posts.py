from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def my_posts(request):
    posts = request.user.posts.order_by('-id') 
    page = request.GET.get('page')
    paginator = Paginator(posts, 2)

    return render(request, 'pages/my_posts.html', context={
        'posts': paginator.get_page(page)
    })