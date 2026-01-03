from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()
class PostManager(models.Manager):
    def filter(self, *args,**kwargs):
        return self.get_queryset().filter(archived=False).filter(*args,**kwargs)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    templates = models.ManyToManyField(to='PostTemplate')
    archived = models.BooleanField(default=False)

    not_archived = PostManager()

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class PostTemplate(models.Model):
    title_template = models.CharField(max_length=100)
    content_template = models.TextField()

    def __str__(self):
        return self.title_template
