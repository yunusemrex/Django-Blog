from django.shortcuts import get_object_or_404, render, redirect
from blogapp.forms import EditsPostModelForm
from blogapp.models import PostModel
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.urls import reverse,  reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    template_name = 'pages/edit-post.html'
    fields = ('title','content','image','author')

    def get_object(self):
        post = get_object_or_404(
            PostModel,
            slug = self.kwargs.get('slug'),
            author = self.request.user            
        )
        return post

    def get_success_url(self):
        return reverse('detail', kwargs={
            'slug': self.get_object().slug
        })       



# @login_required(login_url='/')
# def edit_post(request, slug):
#     post = get_object_or_404(PostModel, slug=slug, author=request.user)
#     form = EditsPostModelForm(request.POST or None, files=request.FILES or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('detail', slug=post.slug)


#     return render(request, 'pages/edit-post.html', context={
#         'form' : form
#     })  