from django.conf.urls import url
from django.contrib import admin
from blog_posts import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog_posts/$', views.post_home),
]
