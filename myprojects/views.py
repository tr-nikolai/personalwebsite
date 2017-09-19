from django.shortcuts import render
from django.db.models import Q
from .forms import MyProjectForm
from .models import MyProject


def my_project(request):
    qs_l = MyProject.objects.all()
    form = MyProjectForm(request.POST or None)
    cleaned_from = None
    if form.is_valid():
        cleaned_from = form.cleaned_data
        count= 0
        for key, value in cleaned_from.items():
            if value == False:
                cleaned_from[key] = None
                count +=1
                if count == len(cleaned_from):
                    context = {
                        'form': form,
                        'title_projects': 'active-link',
                        'qs_l': qs_l,
                    }
                    return render(request, 'form_projects.html', context)
        project_python = cleaned_from.get('project_python')
        project_django = cleaned_from.get('project_django')
        project_sql = cleaned_from.get('project_sql')
        project_html = cleaned_from.get('project_html')
        project_css = cleaned_from.get('project_css')
        qs_l = qs_l.filter(
            Q(project_python=project_python) |
            Q(project_django= project_django) |
            Q(project_sql=project_sql) |
            Q(project_html=project_html) |
            Q(project_css=project_css)
        )
    context = {'form':form,
               'title_projects': 'active-link',
               'qs_l':qs_l,
               'cleaned_form': cleaned_from,
    }
    return render(request, 'form_projects.html', context)