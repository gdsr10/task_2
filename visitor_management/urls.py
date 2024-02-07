# visitor_management/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('visitors/', views.VisitorListView.as_view(), name='visitor_list'),
    path('employee/add/', views.employee_add, name='employee_add'),
    path('employee/edit/<int:employee_id>/', views.employee_edit, name='employee_edit'),
    path('employee/delete/<int:employee_id>/', views.employee_delete, name='employee_delete'),
    path('visitor/add/', views.visitor_add, name='visitor_add'),
    path('visitor/edit/<int:pk>/', views.visitor_edit, name='visitor_edit'),
    path('visitor/delete/<int:pk>/', views.visitor_delete, name='visitor_delete'),
]
