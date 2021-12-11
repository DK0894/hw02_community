from django.shortcuts import get_object_or_404, render

from .models import Group, Post

SHOW_POSTS = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:SHOW_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    posts = group.groups.all()[:SHOW_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
