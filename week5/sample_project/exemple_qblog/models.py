
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    Email = models.EmailField()
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

class Post(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-create_date']

class Comment(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-create_date']



