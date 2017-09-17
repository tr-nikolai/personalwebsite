from django.shortcuts import render
from .models import BlogComments
from django.shortcuts import get_object_or_404, Http404, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages

def comment_delete(request, id):
    try:
        obj = BlogComments.objects.get(id=id)
    except:
        Http404
    if obj.user != request.user:
        response = HttpResponse('У вас нет прав удалить этот комментарий.')
        response.status_code = 403
        return response
    if request.method == 'POST':
        print('POST'*20)
        parent_obj_url = obj.content_object.get_absolute_url()
        obj.delete()
        messages.success(request, 'комментарий удален')
        return HttpResponseRedirect(parent_obj_url)

    context = {
        'object': obj,
    }
    return render(request, 'confirm_delete.html', context)
