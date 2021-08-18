# from blog.blogapp.models.category import CategoryModel
from django.contrib import admin
from .models.category import CategoryModel
from .models.post import PostModel
from .models.comment import CommentModel
from .models.contact import ContactModel


@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content',)
    list_display = ('title', 'created_date', 'updated_date',)


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenter','created_date','updated_date')
    search_fields = ('commenter__username',)


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email' , 'created_date')
    search_fields = ('email',)


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name','slug')
