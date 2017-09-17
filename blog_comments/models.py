from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



class BlogCommentsManager(models.Manager):
    def filter_by_instance(self, instance):
        content_type =  ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(BlogCommentsManager, self).filter(content_type=content_type, object_id=obj_id)
        return qs


class BlogComments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    objects = BlogCommentsManager()

    def __str__(self):
        return str(self.user.username)
