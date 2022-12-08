from django.shortcuts import render
import json

from django.http import HttpResponse

from .models import Employee, Position


def get_position(request):
    positions = Position.objects.all()
    data = []
    for position in positions:
        obj = {'name': position.name, 'department': position.department}
        data.append(obj)
    return HttpResponse(json.dumps(data))


def new_position(request):
    name = request.GET.get('name')
    department = request.GET.get('department')
    position = Position.objects.create(name=name, department=department)
    obj = {'name': position.name, 'department': position.department}
    return HttpResponse(json.dumps(obj))


# ===============================================

def get_employees(request):
    employees = Employee.objects.all()
    data = []
    for employee in employees:
        obj = {'position': employee.position.name, 'salary': employee.salary,
               'fullname': employee.fullname, 'date_birth': str(employee.date_birth)}
        data.append(obj)
    return HttpResponse(json.dumps(data))


def new_employees(request):
    # date_birth = request.GET.get('date_birth')
    fullname = request.GET.get('fullname')
    salary = request.GET.get('salary')
    position = request.GET.get('position')
    position_name = Position.objects.get(name=position)
    employee = Employee.objects.create(fullname=fullname, salary=salary, position=position_name)
    obj = {'fullname': fullname, 'salary': salary, 'position':employee.position.name}
    return HttpResponse(json.dumps(obj))


