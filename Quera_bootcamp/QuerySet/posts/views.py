import datetime

from django.http import HttpResponse
from django.shortcuts import render

from posts.models import Post

# Create your views here.
def retrive_posts(request):
    posts = Post.objects.filter()

    if 'title' in request.GET.keys() and posts.count() > 10:
        posts = posts.filter(title__in=request.GET.getlist('title'))

    if 'content' in request.GET.keys() and posts.count() > 10:
        posts = posts.filter(content=request.GET.get('content'))

    return HttpResponse(f'post count: {posts.count()}')

def retrive_posts_exclude_sample(request):
    posts = Post.objects.all()
    if 'title' in request.GET.keys():
        posts = posts.exclude(title=request.GET.get('title'))
    posts = posts.order_by('-title', 'content')
    posts = posts.filter(created_date__lte =datetime.datetime.now())
    return HttpResponse(posts.only('title').values_list('title', flat=True))


    # messege = f'post count: {posts.count()}'
    # return HttpResponse(messege)



