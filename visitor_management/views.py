# views.py

from django.shortcuts import render, redirect, get_object_or_404
from visitor_management.forms import EmployeeForm, VisitorForm
from .models import Employee, Visitor
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import authentication, permissions


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# from rest_framework.response import Response

# class CustomAuthToken(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })


class EmployeeListView(APIView):
    
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        employees = Employee.objects.all()
        return render(request, 'employee/employee_list.html', {'employees': employees})


class VisitorListView(APIView):
    
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        visitors = Visitor.objects.all()
        return render(request, 'visitor/visitor_list.html', {'visitors': visitors})

@login_required
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee/employee_add_edit.html', {'form': form})

@login_required
def employee_edit(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/employee_add_edit.html', {'form': form})

@login_required
def employee_delete(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee/employee_delete.html', {'employee': employee})

@login_required
def visitor_add(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitor_list')
    else:
        form = VisitorForm()
    return render(request, 'visitor/visitor_add_edit.html', {'form': form})

@login_required
def visitor_edit(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == 'POST':
        form = VisitorForm(request.POST, instance=visitor)
        if form.is_valid():
            form.save()
            return redirect('visitor_list')
    else:
        form = VisitorForm(instance=visitor)
    return render(request, 'visitor/visitor_add_edit.html', {'form': form})

@login_required
def visitor_delete(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == 'POST':
        visitor.delete()
        return redirect('visitor_list')
    return render(request, 'visitor/visitor_delete.html', {'visitor': visitor})
