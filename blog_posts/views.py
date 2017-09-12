from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.http import HttpResponse


def post_create(request):
    return HttpResponse('<h1>create</>')


def post_detail(request, id):
    instance = get_object_or_404(BlogPost, id=id)
    context = {'instance': instance, 'id':id}
    return render(request, 'post_detail.html', context)


def post_list(request):
    queryset = BlogPost.objects.all()
    context = {
        'object_list': queryset,
        'title': 'List',
    }
    return render(request, 'blog.html', context)


def post_update(request):
    return HttpResponse('<h1>update</>')


def post_delete(request):
    return HttpResponse('<h1>delete</>')