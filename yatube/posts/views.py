from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Group, Post, User


def index(request):
    template = 'posts/index.html'
    post_list = Post.objects.all()
    peginator = Paginator(post_list, settings.SHOW_POSTS)
    page_number = request.GET.get('page')
    page_obj = peginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    post_list = group.posts.all()
    peginator = Paginator(post_list, settings.SHOW_POSTS)
    page_number = request.GET.get('page')
    page_obj = peginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    user = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author=user)
    peginator = Paginator(post_list, settings.SHOW_POSTS)
    page_number = request.GET.get('page')
    page_obj = peginator.get_page(page_number)
    post_count = Post.objects.filter(author=user).count()
    context = {
        'username': username,
        'page_obj': page_obj,
        'post_count': post_count,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)
