from django.contrib.auth.decorators import login_required
from django.http import request
from blogapp.models import PostModel
from django.shortcuts import redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy

class DeletePostView(DeleteView):
    template_name = 'pages/delete-post-confirm.html'
    success_url = reverse_lazy('index')


    def get_queryset(self):
        post = PostModel.objects.filter(slug = self.kwargs['slug'], author = self.request.user)
        return post



# @login_required(login_url='/')
# def delete_post(request, slug):
#     get_object_or_404(PostModel, slug=slug, author=request.user).delete()
#     return redirect('index')