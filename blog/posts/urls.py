from django.urls import path
from . import api_views
from .api_views_class import PostList, PostDetail

urlpatterns = [
    path('categories/', api_views.category_list),
    path('categories/<int:pk>/', api_views.category_detail),

    path('topics/', api_views.topic_list),
    path('topics/<int:pk>/', api_views.topic_detail),

    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]
