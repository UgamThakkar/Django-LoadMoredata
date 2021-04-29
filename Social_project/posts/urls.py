from django.urls import path
from posts.views import post_view, PostJsonListView

# app_name = 'posts'

urlpatterns = [
    path('', post_view, name='post-list'),
    path('posts-json/<int:num_posts>', PostJsonListView.as_view(), name='post-json-view'),
]
