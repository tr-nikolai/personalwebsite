from django.shortcuts import render
from django.db.models import Q
from .forms import MyProjectForm
from .models import MyProject


def my_project(request):
    queryset_list = MyProject.objects.all()
    #print(queryset_list)
    form = MyProjectForm(request.POST or None)
    qs_l = None
    if form.is_valid():
        cleaned_from = form.cleaned_data
        for key, value in cleaned_from.items():
            if value == False:
                cleaned_from[key] = None
        project_python = cleaned_from.get('project_python')
        project_django = cleaned_from.get('project_django')
        project_sql = cleaned_from.get('project_sql')
        project_html = cleaned_from.get('project_html')
        project_css = cleaned_from.get('project_css')
        qs_l = queryset_list.filter(
            Q(project_python=project_python) |
            Q(project_django= project_django) |
            Q(project_sql=project_sql) |
            Q(project_html=project_html) |
            Q(project_css=project_css)
        )
        context = {'form': form,
                   'title_projects': 'active-link',
                   'qs_l': qs_l,}
        return render(request, 'form_projects.html', context)

    context = {'form':form,
               'title_projects': 'active-link',
    }
    return render(request, 'form_projects.html', context)