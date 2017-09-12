from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog_posts.urls', namespace='blog')),
]
