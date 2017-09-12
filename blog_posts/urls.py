from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.post_detail, name='detail'),
    url(r'^create/$', views.post_create),
    url(r'^list/$', views.post_list),
    url(r'^update/$', views.post_update),
    url(r'^delete/$', views.post_delete),

]
