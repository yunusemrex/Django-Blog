from django.urls import path
from blogapp.views import contact, category, my_posts, detail, index, add_post, edit_post, delete_post


urlpatterns = [
    path('', index, name='index'),
    path('iletisim/', contact, name='contact'),
    path('category/<slug:category_Slug>', category, name='category'),
    path('posts/', my_posts, name='my_posts'),
    path('detail/<slug:slug>', detail, name='detail'),
    path('add-post/', add_post, name='add_post'),
    path('edit-post/<slug:slug>', edit_post, name='edit_post'),
    path('delete-post/<slug:slug>', delete_post, name='delete_post'),

]
