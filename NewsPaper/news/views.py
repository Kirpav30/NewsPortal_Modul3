from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post
from .filters import PostFilter


class PostsList(ListView):
    model = Post
    ordering = 'dateCreate'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostSearch(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'post_search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostUpdate(LoginRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(LoginRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class ArticleList(ListView):
    model = Post
    ordering = 'dateCreate'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class ArticleDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class ArticlesCreate(LoginRequiredMixin, CreateView):
    permission_required = ('news.add_article',)
    form_class = PostForm
    model = Post
    template_name = 'articles_edit.html'


class ArticlesUpdate(LoginRequiredMixin, UpdateView):
    permission_required = ('news.change_article',)
    form_class = PostForm
    model = Post
    template_name = 'articles_edit.html'


class ArticlesDelete(LoginRequiredMixin, DeleteView):
    permission_required = ('news.delete_article',)
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('article_list')

