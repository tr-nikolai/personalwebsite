from django.shortcuts import render
from myprojects.models import MyProject

def index(request):
    project_list = MyProject.objects.all()[:3]
    first_project = MyProject.objects.all()[0]
    print(first_project)
    second_project = MyProject.objects.all()[1]
    print(second_project)
    third_project = MyProject.objects.all()[2]
    print(third_project)
    context ={
        'title_index': 'active-link',
        'first_project': first_project,
        'second_project': second_project,
        'third_project':third_project,
    }
    return render(request, 'index.html', context)