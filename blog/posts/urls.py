from django.urls import path
from . import api_views

urlpatterns = [
    path('categories/', api_views.category_list),
    path('categories/<int:pk>/', api_views.category_detail),

    path('topics/', api_views.topic_list),
    path('topics/<int:pk>/', api_views.topic_detail),

    path('posts/', api_views.post_list),
    path('posts/<int:pk>/', api_views.post_detail),
]
