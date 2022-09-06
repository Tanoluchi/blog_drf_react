from django.urls import path

from .views import *

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<str:post_slug>/', PostDetailView.as_view(), name='post_detail'),
]
