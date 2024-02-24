from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CompanyForm, DepartmentForm
from .models import Company, Department
from employee.models import Employee

def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'company_form.html', {'form': form})

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})

def company_detail(request, company_name):
    company = get_object_or_404(Company, name=company_name)
    
    if request.method == 'POST':
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
    
    context = {
        'company': company,
        'company_form': company_form,
        'department_form': department_form,
        'departments': departments,
    }

    return render(request, 'company_detail.html', context)

def update_company(request, company_name):
    company = get_object_or_404(Company, name=company_name)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_detail', company_name=company.name)
    else:
        form = CompanyForm(instance=company)
    return render(request, 'company_form.html', {'form': form})

def update_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
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
