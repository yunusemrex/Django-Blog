from django.shortcuts import render, redirect
from blogapp.forms import AddPostModelForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from blogapp.models import PostModel
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class AddPostCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = 'pages/add-post.html'
    model = PostModel
    fields = ('title','content','image','categories')


    def get_success_url(self):
        return reverse('detail', kwargs={
            'slug': self.object.slug
        })


    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        form.save_m2m()
        return super().form_valid(form) 


# @login_required(login_url='/')
# def add_post(request):
#     form = AddPostModelForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         post = form.save(commit=False)
#         post.author = request.user
#         post.save()
#         form.save_m2m()
#         return redirect('detail', slug=post.slug)

#     return render(request, 'pages/add-post.html', context={
#         'form':form
#     })