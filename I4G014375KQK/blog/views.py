from django.urls import reverse_lazy
from django.views import generic

from I4G014375KQK.blog.models import Post

post = Post()


class PostListView(generic.ListView):
    model = Post


class PostCreateView(generic.CreateView):
    model = Post
    field = "__all__"
    success_url = reverse_lazy("blog:all")


class PostDetailView(generic.DetailView):
    model = Post


class PostUpdateView(generic.UpdateView):
    model = Post
    field = "__all__"
    success_url = reverse_lazy("blog:all")


class PostDeleteView(generic.DeleteView):
    model = Post
    field = "__all__"
    success_url = reverse_lazy("blog:all")
