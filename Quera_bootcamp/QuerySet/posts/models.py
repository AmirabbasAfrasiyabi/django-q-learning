from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()

class PostManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        return queryset.filter(archived=False)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(to =User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    view_count = models.PositiveSmallIntegerField(default=0)
    like_count = models.PositiveSmallIntegerField(default=0)
    dislike_count = models.PositiveSmallIntegerField(default=0)
    engagement_count = models.PositiveIntegerField()
    templates = models.ManyToManyField(to='PostTemplate', related_name='posts')
    archived = models.BooleanField(default=False)
    not_archived = PostManager()


    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='my_comments')

    def __str__(self):
        return self.text


class PostTemplate(models.Model):
    title_template = models.CharField(max_length=64)
    content_template = models.TextField()

    def __str__(self):
        return f"title: {self.title_template}"