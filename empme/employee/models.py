from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from company.models import Company, Department

class Employee(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name = 'employees', null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name = 'employees', null=True, blank=True)
    position = models.CharField(max_length=255)
    email = models.EmailField()

    def is_company(self, company_id):
        return self.is_superuser == True or (self.company.id==company_id and self.is_staff)

    def __str__(self):
        return f'{self.first_name} {self.last_name}' if self.first_name or self.last_name else 'N/A'

from datetime import datetime
from django.db import models

class Workflow(models.Model):
    STATUS_CHOICES = [
        ('application received', 'Application Received'),
        ('interview scheduled', 'Interview Scheduled'),
        ('hired', 'Hired'),
        ('rejected', 'Rejected'),
        ('fired', 'Fired'),
    ]

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='work_flow')
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='work_flow', blank=True, null=True)
    date = models.DateField(auto_now=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='application received')

    def __str__(self):
        days_ago = (datetime.now().date() - self.date).days
        return f'{self.status} {days_ago} days ago'
