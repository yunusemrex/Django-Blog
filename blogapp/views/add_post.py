from django.shortcuts import render, redirect
from blogapp.forms import AddPostModelForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from blogapp.models import PostModel


class AddPostCreateView(CreateView):
    template_name = 'pages/add-post.html'
    model = PostModel
    fields = ('title','content','image','categories')
    

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