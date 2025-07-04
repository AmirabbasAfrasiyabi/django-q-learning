from datetime import datetime, timedelta

from django.http import HttpResponse
from posts.models import Post

def retrive_posts(request):
    posts = Post.objects.all()

    if 'author' in request.GET.keys():
        posts = posts.filter(author_iexact=request.GET.get('author'))


    if 'content' in request.GET.keys():
        posts = posts.filter(content=request.GET.get ['content'])

    massage = f'post count: {posts.count()}'
    return HttpResponse(massage)

def retrieve_posts_exclude_sample(request, posts=None):
    posts = Post.objects.filter()

    if 'title' in request.GET.keys():
        posts = posts.exclude(title=request.GET.get('title'))

    posts = posts.order_by('-title', 'content')
    posts = posts.filter(created_at__range=(datetime.now() - timedelta(hours=1), datetime.now()))
    # massage = f'post count: {posts.count()}'
    return HttpResponse(posts.only('title').values_list('title', flat=False))


