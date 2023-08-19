from django.urls import path

from .views import PostsView, PostDetail, CreatePost

urlpatterns = [
    path('<uuid:pk>/', PostDetail.as_view(), name='detail-post'),
    path('create/', CreatePost.as_view(), name='create-post'),
]