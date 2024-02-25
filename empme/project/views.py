from django.http import  HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProjectForm
from .models import Project
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required
def project_create(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})

@login_required
def project_list(request):
    project_list = Project.objects.all()
    paginator = Paginator(project_list, 10)

    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results.
        projects = paginator.page(paginator.num_pages)

    return render(request, 'project_list.html', {'projects': projects})

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        
        if not (request.user.is_superuser or request.user.is_company(project.company.id)):
            return HttpResponseForbidden("You don't have permission to access this page.")
        
        # Check if the request is for updating the project details
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project_id)
        
        # Check if the request is for deleting the project
        if 'delete' in request.POST:
            project.delete()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'project_detail.html', {'project': project, 'form': form})