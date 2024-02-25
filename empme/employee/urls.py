from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('register/', views.employee_register, name='employee_register'),
    path('<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
