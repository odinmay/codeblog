from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Post


class PostHome(View):
    template_name = 'blog_home.html'

    def get(self, request):
        return render(request, self.template_name)

class PostList(ListView):
    queryset = Post.objects.filter(status=0).order_by('-created_on')
    template_name = 'post_list.html'


class PostDetail(DetailView):
    template_name = 'post_detail.html'
    model = Post

