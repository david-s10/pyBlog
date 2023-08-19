from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import PostForm
from .models import Post


# Create your views here.


class PostsView(ListView):
    template_name = 'feed.html'
    model = Post
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/post_detail.html'


class CreatePost(CreateView):
    template_name = 'posts/post_create.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user-profile', args=[self.request.user.id])

