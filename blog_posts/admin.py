from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title','updated', 'timestamp', ]
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'content']

    class Meta:
        model = BlogPost

admin.site.register(BlogPost, BlogPostAdmin)
