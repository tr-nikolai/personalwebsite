from django import forms

from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'content',
            'image',
            'draft',
            'publish'
        ]