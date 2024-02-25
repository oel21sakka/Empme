from django.contrib import admin
from .models import Employee, Workflow

admin.site.register([Employee, Workflow])
