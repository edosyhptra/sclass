from django.urls import path
from app_blog.views import create, list, read, update, delete

urlpatterns = [
    path('create/', create.view, name='app_blog'),
    path('list/', list.view, name='list_blog'),
    path('read/<int:id>/', read.view, name='read_blog'),
    path('update/<int:id>/', update.view, name='blog_update'),
    path('delete/<int:id>/', delete.view, name='blog_delete'),
]