from django.shortcuts import render, redirect
from blogapp.forms import AddPostModelForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def add_post(request):
    form = AddPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        form.save_m2m()
        return redirect('detail', slug=post.slug)

    return render(request, 'pages/add-post.html', context={
        'form':form
    })