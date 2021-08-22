from django.shortcuts import render, get_object_or_404
from blogapp.models import CategoryModel
from django.views.generic import ListView

# from django.core import paginator
# from django.core.paginator import Paginator

class CategoryListView(ListView):
    template_name = 'pages/category.html'
    context_object_name = 'posts'
    paginate_by = 2
    
    def get_queryset(self):
        category = get_object_or_404(CategoryModel, slug = self.kwargs['category_Slug'])
        return category.post.all()

        


# def category(request, category_Slug):
#     category = get_object_or_404(CategoryModel, slug=category_Slug)
#     posts = category.post.order_by('-id')
#     page = request.GET.get('page')

#     paginator = Paginator(posts, 2)

#     return render(request, 'pages/category.html', context={
#         'posts': paginator.get_page(page),
#         'category_name': category.name  
#     })