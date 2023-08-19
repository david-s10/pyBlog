from django.urls import path

from .views import HomeView
from posts.views import PostsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('feed/', PostsView.as_view(), name='feed')
]