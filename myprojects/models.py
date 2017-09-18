from django.db import models


class MyProject(models.Model):
    project_name = models.CharField(max_length=100)
    project_short_description = models.TextField(blank=True, null=True)
    project_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    #urlgit = models.URLField

    project_python = models.BooleanField(default=False)
    project_django = models.BooleanField(default=False)
    project_sql = models.BooleanField(default=False)
    project_html = models.BooleanField(default=False)
    project_css = models.BooleanField(default=False)


    def __str__(self):
        return self.project_name
