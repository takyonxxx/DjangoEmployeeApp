from django.shortcuts import render, redirect
from rest_framework.response import Response

from djangoemployeeapp.base_view import BaseViewSet
from .models import Employee
# Create your views here.
from .serializers import EmployeeSerializer


def index(request):
    employees = Employee.objects.all()
    return render(request, "index.html", {'employees': employees})


class EmployeeViewSet(BaseViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    search_fields = ['id', 'name', 'status']

    def list(self, request, *args, **kwargs):

        employees = Employee.objects.all()

        employees_ = self.filter_queryset(employees)
        if employees_:
            page = self.paginate_queryset(employees_)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                resp = self.get_paginated_response(serializer.data)
                return resp

        serializer = self.get_serializer(employees_, many=True)
        return Response({'result': serializer.data})

    def retrieve(self, request, *args, **kwargs):
        _id = request.data.get('id') or ''

        employee = Employee.objects.filter(id=_id)

        employee_ = self.filter_queryset(employee)
        if employee_:
            page = self.paginate_queryset(employee_)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                resp = self.get_paginated_response(serializer.data)
                return resp

        serializer = self.get_serializer(employee_, many=True)
        return Response({'result': serializer.data})

    def create(self, request, *args, **kwargs):
        _name = request.data.get('name') or ''
        new_employee = Employee(name=_name, status=False)
        new_employee.save()

        return redirect('/')

    def update(self, request, *args, **kwargs):
        _id = request.data.get('id') or ''
        employee = Employee.objects.filter(id=_id).first()
        employee.status = not employee.status
        employee.save()
        return redirect('/')

    def destroy(self, request, *args, **kwargs):
        _id = request.data.get('id') or ''
        employee = Employee.objects.filter(id=_id)
        employee.delete()
        return redirect('/')
