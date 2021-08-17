from blogapp.views import my_posts
from blogapp.views.index import index
from django.urls import path
from blogapp.views import contact, category, my_posts


urlpatterns = [
    path('', index, name='index'),
    path('iletisim/', contact, name='contact'),
    path('category/<slug:category_Slug>', category, name='category'),
    path('posts/', my_posts, name='my_posts')
]
