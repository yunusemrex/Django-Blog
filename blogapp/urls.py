from blogapp.views.delete_comment import delete_comment
from django.urls import path
from blogapp.views import ContactFormView , CategoryListView, my_posts, DetailView, index, AddPostCreateView, PostUpdateView, DeletePostView, delete_comment
from django.views.generic import TemplateView, RedirectView


urlpatterns = [
    path('', index, name='index'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('email-sent/', TemplateView.as_view(
        template_name = 'pages/email-sent.html'
    ), name='email-sent'),
    path('about/', TemplateView.as_view(
        template_name = 'pages/about.html'    
    ), name='about'),
    path('category/<slug:category_Slug>', CategoryListView.as_view(), name='category'),
    path('posts/', my_posts, name='my_posts'),  
    path('detail/<slug:slug>', DetailView.as_view(), name='detail'),
    path('add-post/', AddPostCreateView.as_view(), name='add_post'),
    path('edit-post/<slug:slug>', PostUpdateView.as_view(), name='edit_post'),
    path('delete-post/<slug:slug>', DeletePostView.as_view(), name='delete_post'),
    path('delete-comment/<int:id>', delete_comment, name='delete_comment'),
    path('redirect', RedirectView.as_view(
        url='https://inonusosyal.com'
    ), name='redirect'),

    

]
