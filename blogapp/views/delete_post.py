from django.contrib.auth.decorators import login_required
from blogapp.models import PostModel
from django.shortcuts import get_object_or_404, redirect


@login_required(login_url='/')
def delete_post(request, slug):
    get_object_or_404(PostModel, slug=slug, author=request.user).delete()
    return redirect('index')