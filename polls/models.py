from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User


class Post(models.Model):
    objects = models.Manager()
    post_heading = models.CharField(max_length=200)
    post_text = models.TextField(max_length=200000)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey(User, on_delete=CASCADE, related_name='author_posts', null=True)
    likes = models.ManyToManyField(User, related_name='likes_on_post', blank=True)
    is_liked = models.BooleanField(False)
