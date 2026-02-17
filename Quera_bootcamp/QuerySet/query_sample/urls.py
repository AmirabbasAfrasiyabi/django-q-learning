"""
URL configuration for query_sample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from posts.views import (retrive_posts ,
                         retrive_posts_exclude_sample ,
                         retrive_posts_with_equal_content_title,
                         get_comments,
                         add_templates
                         )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',retrive_posts),
    path('posts/exclude/',retrive_posts_exclude_sample) ,
    path('posts/same_title/',retrive_posts_with_equal_content_title),
    path('posts/comment/',get_comments),
    path('posts/templates/',add_templates),
]
