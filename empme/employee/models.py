from django.contrib.auth.models import AbstractUser
from django.db import models
from company.models import Company, Department

class Employee(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name = 'employees', null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name = 'employees', null=True, blank=True)
    position = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def is_company(self, company_id):
        return self.is_superuser == True or (self.company.id==company_id and self.is_staff)

    def __str__(self):
        return f'{self.first_name} {self.last_name}' if self.first_name or self.last_name else 'N/A'
