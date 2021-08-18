from django.db import models
from django.db.models.fields import TextField
from blogapp.models import PostModel
from blogapp.abstract_model import DateAbstractModel


class CommentModel(DateAbstractModel):
    commenter = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    comment = TextField()


    class Meta:
        db_table = 'comment'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.commenter.username  