from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import index
from accounts.views import (register_view, login_view, logout_view)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog_posts.urls', namespace='blog')),
    url(r'^comments/', include('blog_comments.urls', namespace='comments')),
    url(r'^myprojects/', include('myprojects.urls', namespace='myprojects')),
    url(r'^register/$', register_view, name='register'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^$', index),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
