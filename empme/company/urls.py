from django.urls import path
from . import views

urlpatterns = [
    path('', views.company_list, name='company_list'),
    path('create/', views.create_company, name='create_company'),
    path('get_departments/', views.get_departments, name='get_departments'),
    path('<str:company_name>/', views.company_detail, name='company_detail'),
    path('<str:company_name>/update/', views.update_company, name='update_company'),
    path('departments/<int:department_id>/update/', views.update_department, name='update_department'),
]
