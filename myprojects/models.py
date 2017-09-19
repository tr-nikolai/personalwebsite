from django.db import models


class MyProject(models.Model):
    project_name = models.CharField(max_length=100)
    project_short_description = models.TextField(blank=True, null=True)
    project_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    urlgit = models.URLField(null=True, blank=True)

    project_python = models.BooleanField(default=False, verbose_name='Python 3')
    project_django = models.BooleanField(default=False, verbose_name='Django')
    project_sql = models.BooleanField(default=False, verbose_name='SQL')
    project_html = models.BooleanField(default=False, verbose_name='HTML 5')
    project_css = models.BooleanField(default=False, verbose_name='CSS 3')
    class Meta:
        ordering = ['-project_timestamp']


    def __str__(self):
        return self.project_name
