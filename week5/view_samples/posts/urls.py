from django.urls import path

from posts.views import retrieve_posts, retrieve_post_info, retrieve_post_text, create_post , retrieve_post_file

urlpatterns = [
    path('', retrieve_posts),
    path('create/',create_post),
    path('<int:pk>/<str:name>/', retrieve_post_file),
    path('<int:pk>/', retrieve_post_file),
    path('<int:pk>/text', retrieve_post_text),
]
