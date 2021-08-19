from django.urls import path
from account.views import log_out

urlpatterns = [
    path('log-out', log_out, name='log-out')
]
