from django.urls import path
from blogapp.views import contact, category, my_posts, detail, index


urlpatterns = [
    path('', index, name='index'),
    path('iletisim/', contact, name='contact'),
    path('category/<slug:category_Slug>', category, name='category'),
    path('posts/', my_posts, name='my_posts'),
    path('detail/<slug:slug>', detail, name='detail'),

]
