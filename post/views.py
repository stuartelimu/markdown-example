from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

class IndexView(TemplateView):
    template_name = 'index.html'

    
class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'body']


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'body']


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')
