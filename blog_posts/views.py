from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import BlogPost
from .forms import BlogPostForm


def post_create(request):
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Пост создан!')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, 'Пост не был создан!')
    context = {
        'form': form,
    }
    return render(request, 'post_form.html', context)


def post_list(request):
    queryset = BlogPost.objects.all()
    context = {
        'object_list': queryset,
        'title': 'List',
    }
    return render(request, 'blog.html', context)


def post_update(request, id=id):
    instance = get_object_or_404(BlogPost, id=id)
    form = BlogPostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Пост обновлен!')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {'instance': instance,
               'id': id,
               'form': form,
               }
    return render(request, 'post_form.html', context)


def post_detail(request, id=id):
    instance = get_object_or_404(BlogPost, id=id)
    context = {
        'title': instance.title,
        'instance': instance,
    }
    return render(request, 'post_detail.html', context)


def post_delete(request, id=id):
    instance = get_object_or_404(BlogPost, id=id)
    instance.delete()
    messages.success(request, 'Пост создан!')
    return redirect('blog:list')

