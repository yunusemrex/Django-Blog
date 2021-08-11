# from blog.blogapp.models.category import CategoryModel
from django.contrib import admin
from .models.category import CategoryModel
from .models.post import PostModel

class PostAdmin(admin.ModelAdmin):
    search_fields = ('title','content')
    list_display = ('title', 'created_date','edited_date')


admin.site.register(CategoryModel)
admin.site.register(PostModel)