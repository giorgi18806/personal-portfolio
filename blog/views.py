from django.shortcuts import render, get_object_or_404

from blog.models import Blog


def index(request):
    context = {
        'blogs': Blog.objects.all(),
    }

    return render(request, 'blog/index.html', context)


def detail(request, pk):
    context = {
        'blog': get_object_or_404(Blog, pk=pk)
    }

    return render(request, 'blog/detail.html', context)


