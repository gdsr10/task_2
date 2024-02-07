# visitor_management/forms.py

from django import forms
from .models import Employee, Visitor

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'office_location', 'department']


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'email', 'office_location', 'employee_visiting', 'status']
        widgets = {
            'status': forms.Select(choices=Visitor.STATUS_CHOICES)
        }