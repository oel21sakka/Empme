from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeView.as_view(), name='api_company_list'),
    path('companies/', views.CompanyView.as_view(), name='api_company_list'),
    path('projects/', views.ProjectView.as_view(), name='api_projects_list'),
]
