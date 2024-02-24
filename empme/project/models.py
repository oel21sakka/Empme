from django.db import models
from company.models import Company, Department
from employee.models import Employee

class Project(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='projects', null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='projects', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_employees = models.ManyToManyField(Employee, related_name='projects', blank=True)

    def __str__(self):
        return self.name
