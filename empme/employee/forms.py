from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Employee, Workflow

class EmployeeRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Employee
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'company')

class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'username', 'email', 'company', 'department', 'position']

    def clean(self):
        cleaned_data = super().clean()
        company = cleaned_data.get('company')
        department = cleaned_data.get('department')
        if company and department and department.company != company:
            raise forms.ValidationError("Selected department does not belong to the selected company.")
        return cleaned_data

class WorkFlowForm(forms.ModelForm):
    class Meta:
        model = Workflow
        fields = ['status']