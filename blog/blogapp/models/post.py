from django.db import models
from autoslug import AutoSlugField
from blogapp.models import CategoryModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class PostModel(models.Model):
    image = models.ImageField(upload_to='post-images')
    title = models.CharField(max_length=50)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from = 'title', unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name='post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'Post'
    
    def __str__(self):
        return self.title

 