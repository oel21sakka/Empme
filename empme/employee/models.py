from django.contrib.auth.models import AbstractUser
from django.db import models
from company.models import Company, Department

class Employee(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name = 'employees', null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name = 'employees', null=True, blank=True)
    position = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
