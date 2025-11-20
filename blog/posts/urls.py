from django.urls import path
from . import api_views, views

urlpatterns = [
    path('categories/', api_views.category_list),
    path('categories/<int:pk>/', api_views.category_detail),
    path('categories/<int:pk>/topics/', views.topics_by_category),


    path('topics/', api_views.topic_list),
    path('topics/<int:pk>/', api_views.topic_detail),

    path('posts/', api_views.post_list),
    path('posts/update/<int:pk>/', api_views.post_update),
    path('posts/delete/<int:pk>/', api_views.post_delete),

    path('users/posts/', views.user_posts),
]
