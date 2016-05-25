from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Post(models.Model):
    post_posted = models.DateTimeField('DateTime published')
    post_text = models.TextField(max_length=2000)
    post_likes = models.IntegerField(default=0)
    post_views = models.IntegerField(default=0)
    post_favorited = models.IntegerField(default=0)
    post_dislikes = models.IntegerField(default=0)
    post_image = models.ImageField(upload_to='post/static/post/images')
    post_tags = models.CharField(max_length=1000, default=None)
    post_user = models.CharField(max_length=40, default='Anonymus')

    def __str__(self):
        return self.post_text


class Comment(models.Model):
    comment_posted = models.DateTimeField('DateTime published')
    comment_text = models.TextField(max_length=2000)
    comment_likes = models.IntegerField(default=0)
    comment_views = models.IntegerField(default=0)
    comment_favorited = models.IntegerField(default=0)
    comment_dislikes = models.IntegerField(default=0)
    comment_user = models.CharField(max_length=40, default='Anonymus')
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text

