from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CompanyForm, DepartmentForm
from .models import Company, Department
from employee.models import Employee
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required
def create_company(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'company_form.html', {'form': form})

@login_required
def company_list(request):
    company_list = Company.objects.all()
    paginator = Paginator(company_list, 10)

    page = request.GET.get('page')
    try:
        companies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        companies = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results.
        companies = paginator.page(paginator.num_pages)

    return render(request, 'company_list.html', {'companies': companies})

@login_required
def company_detail(request, company_name):
    company = get_object_or_404(Company, name=company_name)
    
    if request.method == 'POST':
        if not request.user.is_superuser and not request.user.is_company(company.id):
            return HttpResponseForbidden("You don't have permission to access this page.")

        # Check if the request is for updating the company details
        if 'update_company' in request.POST:
            company_form = CompanyForm(request.POST, instance=company)
            if company_form.is_valid():
                company_form.save()
                return redirect('company_detail', company_name=company.name)
        
        # Check if the request is for deleting the company
        elif 'delete_company' in request.POST:
            company.delete()
            return redirect('company_list')

        # Check if the request is for creating a new department
        elif 'create_department' in request.POST:
            department_form = DepartmentForm(request.POST)
            if department_form.is_valid():
                department = department_form.save(commit=False)
                department.company = company  # Set the company
                department.save()
                return redirect('company_detail', company_name = company.name)
        
        # Check if the request is for deleting a department
        elif 'delete_department' in request.POST:
            department_id = request.POST.get('delete_department')
            department = get_object_or_404(Department, id=department_id)
            department.delete()
            return redirect('company_detail', company_name = company.name)
    
    else:
        company_form = CompanyForm(instance=company)
        department_form = DepartmentForm()
    
    departments = company.departments.all()
    employees = company.employees.all()
    
    context = {
        'company': company,
        'company_form': company_form,
        'department_form': department_form,
        'departments': departments,
        'employees': employees,
    }
    return render(request, 'company_detail.html', context)

@login_required
def update_company(request, company_name):

    company = get_object_or_404(Company, name=company_name)
    
    if not request.user.is_company(company.id):
        return HttpResponseForbidden("You don't have permission to access this page.")

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_detail', company_name=company.name)
    else:
        form = CompanyForm(instance=company)
    return render(request, 'company_form.html', {'form': form})

@login_required
def update_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    
    if not request.user.is_company(department.company.id):
            return HttpResponseForbidden("You don't have permission to access this page.")
    
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('company_detail', company_name=department.company.name)
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'department_form.html', {'form': form})

def get_departments(request):
    company_id = request.GET.get('company_id')
    
    try:
        company = Company.objects.get(id=company_id)
        departments = Department.objects.filter(company=company)
        data = [{'id': department.id, 'name': department.name} for department in departments]
        return JsonResponse({'departments': data})
    except:
        return JsonResponse({'departments': []})

def get_employees(request):
    company_id = request.GET.get('company_id')
    
    try:
        company = Company.objects.get(id=company_id)
        employees = Employee.objects.filter(company=company)
        data = [{'id': employee.id, 'name': str(employee)} for employee in employees]
        return JsonResponse({'employees': data})
    except:
        return JsonResponse({'employees': []})
