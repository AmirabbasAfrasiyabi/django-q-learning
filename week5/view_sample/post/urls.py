from django.http import HttpResponse
from django.urls import re_path
from django.urls import path
from post.views import retrieve_posts, retrieve_post_info, retrieve_post_text,create_post

urlpatterns = [
    path('', retrieve_posts),
    path('create', create_post),
    path('<int:pk>/<str:name>', retrieve_post_info),
    path('<int:pk>', retrieve_post_info),
    path('<int:pk>/text', retrieve_post_text),
]
