from django.core import paginator
from django.shortcuts import render, get_object_or_404
from blogapp.models import PostModel, CategoryModel
from django.core.paginator import Paginator

def category(request, category_Slug):
    category = get_object_or_404(CategoryModel, slug=category_Slug)
    posts = category.post.order_by('-id')
    page = request.GET.get('page')

    paginator = Paginator(posts, 2)

    return render(request, 'pages/category.html', context={
        'posts': paginator.get_page(page),
        'category_name': category.name  
    })