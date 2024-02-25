from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from .forms import EmployeeRegistrationForm, EmployeeUpdateForm, WorkFlowForm
from .models import Employee, Workflow
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required
def employee_list(request):
    if request.user.is_superuser:
        employee_list = Employee.objects.all()
    elif request.user.company:
        employee_list = Employee.objects.filter(company=request.user.company)
    else:
        return HttpResponse("No employees in your company.")
    
    
    paginator = Paginator(employee_list, 10)

    page = request.GET.get('page')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        employees = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results.
        employees = paginator.page(paginator.num_pages)

    return render(request, 'employee_list.html', {'employees': employees})

@login_required
def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    
    if request.method == 'POST':
        
        if not (request.user.id == employee_id or
                request.user.is_superuser or
                request.user.is_company(employee.company.id)
            ):
            return HttpResponseForbidden("You don't have permission to access this page.")
    
        # Check if the request is for updating the employee details
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_detail', employee_id=employee_id)
        
        # Check if the request is for deleting the employee
        if 'delete' in request.POST:
            employee.delete()
            return redirect('employee_list')
    else:
        form = EmployeeUpdateForm(instance=employee)
    
    return render(request, 'employee_detail.html', {'employee': employee, 'form': form})

def employee_register(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'employee_register.html', {'form': form})

@login_required
def workflow_list(request):
    if request.user.is_superuser:
        workflows = Workflow.objects.all()
    elif request.user.company and request.user.is_company(request.user.company.id):
        employees = Employee.objects.filter(company=request.user.company)
        workflows = Workflow.objects.filter(employee__in=employees)
        print(employees)
    else:
        workflows = Workflow.objects.filter(employee=request.user)
    print(workflows)
    return render(request, 'workflow_list.html', {'workflows': workflows})

@login_required
def workflow_detail(request, workflow_id):
    workflow = get_object_or_404(Workflow, id=workflow_id)
    
    if not (request.user.is_superuser==True or request.user == workflow.employee
            or request.user.is_company(workflow.company.id)):
        return HttpResponseForbidden("You don't have permission to access this page.")
    
    if request.method == 'POST':
        form = WorkFlowForm(request.POST, instance=workflow)
        if form.is_valid():
            form.save()
            return redirect('workflow_list')
    else:
        form = WorkFlowForm(instance=workflow)
    
    return render(request, 'workflow_detail.html', {'form': form, 'workflow': workflow})
