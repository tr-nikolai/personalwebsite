from django.shortcuts import render
from .models import BlogPost
from django.http import HttpResponse


def post_home():
    return HttpResponse('<h1>Hello</>')
