from django.shortcuts import render, get_object_or_404
from blogapp.models import CategoryModel
from django.views.generic import ListView


class CategoryListView(ListView):
    template_name = 'pages/category.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        category = get_object_or_404(CategoryModel, slug = self.kwargs['category_Slug'])
        return category.post.all()

        