from django.shortcuts import get_object_or_404, redirect, render
from .forms import EmployeeRegistrationForm, EmployeeUpdateForm
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    
    if request.method == 'POST':
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