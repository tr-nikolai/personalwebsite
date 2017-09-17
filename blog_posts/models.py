from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone
from blog_comments.models import BlogComments

class BlogPostManager(models.Manager):
    def active(self):
        return super(BlogPostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

class BlogPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_posts',
                              null=True, blank=True,
                              height_field='height_field',
                              width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    objects = BlogPostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'id': self.id})

    class Meta:
        ordering = ['-timestamp', '-updated']

    @property
    def comments(self):
        instance = self
        qs = BlogComments.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type
