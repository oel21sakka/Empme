from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProjectForm
from .models import Project

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
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