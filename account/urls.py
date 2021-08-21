from django.urls import path
from account.views import log_out, Change_Password, edit_profile
from account.views import registration_form


urlpatterns = [
    path('log-out', log_out, name='log-out'),
    path("change-password", Change_Password, name="change-password"),
    path('edit-profile', edit_profile, name='edit-profile'), 
    path('register', registration_form, name='register'),    
]
