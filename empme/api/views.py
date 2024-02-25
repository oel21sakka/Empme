from rest_framework import generics
from . import serializers
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from employee.models import Employee
from company.models import Company
from project.models import Project

class EmployeeView(generics.ListAPIView):
    serializer_class = serializers.EmployeeSerializer
    queryset = Employee.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['username', 'email', 'first_name', 'last_name']
    filterset_fields = ['company', 'department']

class CompanyView(generics.ListAPIView):
    serializer_class = serializers.CompanySerializer
    queryset = Company.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class ProjectView(generics.ListAPIView):
    serializer_class = serializers.ProjectSerializer
    queryset = Project.objects.all()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['start_date','end_date']
    search_fields = ['name']

