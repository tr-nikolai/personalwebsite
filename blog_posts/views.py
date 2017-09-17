from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Q
from .models import BlogPost
from .forms import BlogPostForm
from blog_comments.forms import BlogCommentForm
from blog_comments.models import BlogComments


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = BlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Пост создан!')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'post_form.html', context)


def post_update(request, id=id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(BlogPost, id=id)
    form = BlogPostForm(request.POST or None, request.FILES or None, instance=instance)
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


def post_delete(request, id=id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(BlogPost, id=id)
    instance.delete()
    messages.success(request, 'Пост удалён!')
    return redirect('blog:list')


def post_detail(request, id=id):
    instance = get_object_or_404(BlogPost, id=id)
    today = timezone.now().date()
    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    initial_data = {
        'content_type': instance.get_content_type,
        'object_id': instance.id,
    }
    form = BlogCommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        c_type_cleaned = c_type.replace(' ', '')
        content_type = ContentType.objects.get(model=c_type_cleaned)
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get('content')
        new_comment, created = BlogComments.objects.get_or_create(
            user = request.user,
            content_type = content_type,
            object_id = obj_id,
            content = content_data,
        )
    comments = instance.comments
    context = {
        'title': instance.title,
        'instance': instance,
        'today': today,
        'comments': comments,
        'comment_form': form,
    }
    return render(request, 'post_detail.html', context)


def post_list(request):
    queryset_list = BlogPost.objects.active()
    today = timezone.now().date()
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = BlogPost.objects.all()
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list': queryset,
        'title': 'List',
        'page_request_var':  page_request_var,
        'today': today,
    }
    return render(request, 'blog.html', context)
