from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from blogapp.models import PostModel
from blogapp.forms import AddCommentModelForm, add_comment
from django.views import View


class DetailView(View):
    http_method_names = ['get', 'post']
    add_comment_form = AddCommentModelForm
    
    def get(self, request, slug):
        post = get_object_or_404(PostModel, slug=slug)
        comments = post.comments.all()
        return render(request, 'pages/detail.html', context={
        'post': post,
        'comments': comments,
        'add_comment_form': self.add_comment_form
    })
    
    
    def post(self, request, slug):
        post = get_object_or_404(PostModel, slug=slug)
        add_comment_form = self.add_comment_form(data=request.POST)   
        if add_comment_form.is_valid():
            comment = add_comment_form.save(commit=False)
            comment.commenter = request.user
            comment.post = post
            comment.save()
            messages.success(request,'Comment successfully added.')
        return redirect('detail', slug)


        


# def detail(request, slug):
#     post = get_object_or_404(PostModel, slug=slug)
#     comments = post.comments.all()

#     if request.method == 'POST':
#         add_comment_form = AddCommentModelForm(data=request.POST)   
#         if add_comment_form.is_valid():
#             comment = add_comment_form.save(commit=False)
#             comment.commenter = request.user
#             comment.post = post
#             comment.save()

#     else:
#         add_comment_form = AddCommentModelForm()
#         comments = post.comments.all()


#     return render(request, 'pages/detail.html', context={
#         'post': post,
#         'comments': comments,
#         'add_comment_form': add_comment_form
#     })
 