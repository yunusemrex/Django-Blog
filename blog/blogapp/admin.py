# from blog.blogapp.models.category import CategoryModel
from django.contrib import admin
from .models.category import CategoryModel
from .models.post import PostModel
from .models.comment import CommentModel
from .models.contact import ContactModel

class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content',)
    list_display = ('title', 'created_date', 'edited_date',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenter','created_date','updated_date')
    search_fields = ('commenter__username',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email' , 'created_date')
    search_fields = ('email',)



admin.site.register(CategoryModel)
admin.site.register(PostModel, PostAdmin)
admin.site.register(CommentModel, CommentAdmin)
admin.site.register(ContactModel,ContactAdmin)