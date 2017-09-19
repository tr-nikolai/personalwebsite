from django import forms

from .models import MyProject


class MyProjectForm(forms.ModelForm):
    class Meta:
        model = MyProject
        fields = [
            'project_python',
            'project_django',
            'project_sql',
            'project_html',
            'project_css',
        ]