from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'

