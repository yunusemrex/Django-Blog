from django.contrib import auth
from django.urls import path
from account.views import log_out, Change_Password, edit_profile, registration_form
from django.contrib.auth import login, views as auth_views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(
        template_name = 'pages/login.html'
    ), name='login'),
    path('log-out', log_out, name='log-out'),
    path('change-password', Change_Password, name='change-password'),
    path('edit-profile', edit_profile, name='edit-profile'), 
    path('register', registration_form, name='register'),    
]
