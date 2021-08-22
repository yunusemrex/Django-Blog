from django.views.generic import DetailView
from account.models import CustomUserModel
from django.shortcuts import get_object_or_404

class ProfileDetailView(DetailView):
    template_name = 'pages/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return get_object_or_404(
            CustomUserModel, username = self.kwargs.get('username')
        )