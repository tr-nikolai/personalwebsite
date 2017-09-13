from django.conf.urls import url, include
from django.contrib import admin
from .views import index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^blog/', include('blog_posts.urls', namespace='blog')),
]
