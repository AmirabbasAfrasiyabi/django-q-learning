from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()
class posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
