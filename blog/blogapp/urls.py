from blogapp.views.index import index
from django.urls import path
from blogapp.views import contact, category


urlpatterns = [
    path('', index, name='index'),
    path('iletisim/', contact, name='contact'),
    path('category/<slug:category_Slug>', category, name='category')
]
