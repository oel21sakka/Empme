from rest_framework import serializers
from employee.models import Employee
from company.models import Company
from project.models import Project

class EmployeeSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()
    department = serializers.StringRelatedField()
    
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'username', 'email', 'company', 'department', 'position']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    assigned_employees = serializers.StringRelatedField(many=True)
    company = serializers.StringRelatedField()
    department = serializers.StringRelatedField()
        
    class Meta:
        model = Project
        fields = '__all__'
