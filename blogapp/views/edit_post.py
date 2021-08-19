from django.shortcuts import get_object_or_404, render, redirect
from blogapp.forms import EditsPostModelForm
from blogapp.models import PostModel
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def edit_post(request, slug):
    post = get_object_or_404(PostModel, slug=slug, author=request.user)
    form = EditsPostModelForm(request.POST or None, files=request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('detail', slug=post.slug)


    return render(request, 'pages/edit-post.html', context={
        'form' : form
    })  