"""
URL configuration for view_samp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from posts.views import retrive_posts , retrive_Post_info , retrive_Post_text

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', retrive_posts, name='retrive_posts'),
    path('posts/1' , retrive_Post_info , name='retrive_post_info'),
    path('posts/2', retrive_Post_text, name='retrive_post_text'),
]
