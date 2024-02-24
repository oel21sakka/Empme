from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('register/', views.employee_register, name='employee_register'),
    path('<int:employee_id>/', views.employee_detail, name='employee_detail'),
]
