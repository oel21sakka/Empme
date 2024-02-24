from django import forms
from .models import Company, Department

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']
        
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Company.objects.filter(name=name).exists():
            raise forms.ValidationError('A company with this name already exists.')
        return name

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']
