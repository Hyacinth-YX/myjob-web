from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Post(models.Model):
    userId = models.IntegerField()
    postTitle = models.CharField(max_length=256)
    postBody = models.TextField()
    c_time = models.DateTimeField(auto_now_add=True)
    jobCat = models.IntegerField()

    class Meta:
        db_table = "post"
        verbose_name = '帖子'
        verbose_name_plural = '帖子'


class Comment(models.Model):
    userId = models.IntegerField()
    preCommentId = models.IntegerField()
    commentBody = models.TextField()
    c_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comment"
        verbose_name = '评论'
        verbose_name_plural = '评论'
