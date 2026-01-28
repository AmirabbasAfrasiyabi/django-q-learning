from django.urls import path
from website.views import home, about , contact


urlpatterns = [
    path('' , home , name = 'index'),
    path('about/', about ,name = 'about'),
    path('contact/', contact ,name = 'contact'),
]
