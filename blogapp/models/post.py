from django.db import models
from autoslug import AutoSlugField
from blogapp.models import CategoryModel
from ckeditor.fields import RichTextField
from blogapp.abstract_model import DateAbstractModel



class PostModel(DateAbstractModel):
    image = models.ImageField(upload_to='post-images')
    title = models.CharField(max_length=50)
    content = RichTextField()
    slug = AutoSlugField(populate_from = 'title', unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name='post')
    author = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'Post'
    
    def __str__(self):
        return self.title

 