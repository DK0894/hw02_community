from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


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
