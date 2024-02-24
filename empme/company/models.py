from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name

class Department(models.Model):
    company = models.ForeignKey(Company, on_delete = models.CASCADE, related_name = 'departments')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name