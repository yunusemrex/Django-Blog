import blogapp
from blogapp.forms import add_comment
from django.shortcuts import render, get_object_or_404
from blogapp.models import PostModel
from blogapp.forms import AddCommentModelForm

def detail(request, slug):
    post = get_object_or_404(PostModel, slug=slug)
    comments = post.comments.all()

    if request.method == 'POST':
        add_comment_form = AddCommentModelForm(data=request.POST)   
        if add_comment_form.is_valid():
            comment = add_comment_form.save(commit=False)
            comment.commenter = request.user
            comment.post = post
            comment.save()

    else:
        add_comment_form = AddCommentModelForm()


    return render(request, 'pages/detail.html', context={
        'post': post,
        'comments': comments,
        'add_comment_form': add_comment_form
    })
 