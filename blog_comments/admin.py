from django.contrib import admin
from blog_comments.models import BlogComments


class BlogCommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'timestamp', ]
    list_filter = ['timestamp']
    search_fields = ['user']

    class Meta:
        model = BlogComments


admin.site.register(BlogComments, BlogCommentsAdmin)
