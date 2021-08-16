from blogapp.views.index import index
from django.urls import path
from blogapp.views import contact 


urlpatterns = [
    path('', index, name='index'),
    path('iletisim/', contact, name='contact'),
]
