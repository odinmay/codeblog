from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    queryset = Post.objects.filter(status=0).order_by('-created_on')
    template_name = 'post_list.html'


class PostDetail(DetailView):
    template_name = 'post_detail.html'
    model = Post

