from django.urls import path
from app_blog.views import create, list, read

urlpatterns = [
    path('create/', create.view, name='app_blog'),
    path('list/', list.view, name='list_blog'),
    path('read/<int:id>/', read.view, name='read_blog'),
]