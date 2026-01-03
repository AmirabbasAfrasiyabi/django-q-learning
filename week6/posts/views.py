import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q ,F
from posts.models import Post

from posts.models import Comment


#max 3 queries to db . Min 1 quarries to db
def retrive_posts(request):
    filter_exp=Q()

    if 'title' in request.GET.keys() :
        filter_exp &= Q(title__in=request.GET.getlist('title'))

    if 'content' in request.GET.keys() :
        filter_exp &= Q(content__in=request.GET.getlist('content'))

    posts = Post.objects.filter(filter_exp)
    return HttpResponse(f'post_count: {posts.count()}')


def retrive_posts_exclude_sample(request):
    posts = Post.objects.all()
    #or
    # post =Post,object.filter()

    if 'title' in request.GET.keys():
        posts = posts.exclude(title__iexact=request.GET['title'])

    # posts_second = Post.object.filter(content__icontains=request.GET['content'])

    posts = posts.order_by('-title' , 'content')
    posts = posts.filter(
        created_date__range=(
            datetime.datetime.now() - datetime.timedelta(hours=1),
            datetime.datetime.now()
        )
    )
    post2 = Post.objects.filter(content=request.GET.get('content'))
    posts = posts|post2

    return HttpResponse(posts.only('title').values_list('title', flat=False))


def retrive_posts_with_equal_content_title(request):
    # title = request.GET.get('title')
    # post = Post.object.filter((Q(title__iexact=title) | Q(content__iexact=title)))

    """solution1"""

    # posts = []
    # for posts in Post.objects.all():
    #     if posts.title == posts.content:
    #         posts.append(posts)

    """solution2"""
    posts = Post.objects.filter(title=F('content'))
    return HttpResponse(posts.values_list('title', 'content'))


def get_comment(request):
    now = timezone.now()

    recent_comments = Comment.objects.filter(
        post__title__icontains='post',
        created_date__range=(
            now - timedelta(hours=1),
            now
        )
    )

    posts = Post.objects.filter(
        content__icontains='something',
        comment__in=recent_comments
    ).distinct()

    return HttpResponse(list(posts.values()))


def add_templates(request):
    now = datetime.now()
    PostTemplate.objects.create(title_template='some other template', content_template='')
    new_template = PostTemplate.objects.all()
    post = Post.not_archived.first()
    post.templates.set(new_template)
    return HttpResponse('done')

