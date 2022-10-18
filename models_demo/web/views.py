from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.
from models_demo.web.models import Employee, Department, Project


def info(request):
    employees = Employee.objects.all()
    employees2 = Employee.objects.filter(department=4) \
        .order_by("-last_name", "first_name")

    # `get` returns a single object and throws error when none or multiple results
    # get is not lazy but eager and returns an object but not QuerySet
    department = get_object_or_404(Department, pk=2)

    # `department__name` in `filter` is like `department.name`
    employees3 = Employee.objects\
        .filter(department__name="Repair")\
        .order_by("last_name", "first_name")

    # print(employee_with_id_ten)
    context = {
        "employees": employees,
        "employees2": employees2,
        "employees3": employees3,
        "department": department,
    }
    return render(request, "info.html", context)


def show_all_departments(request):
    all_departments = Department.objects.all()
    context = {"departments": all_departments}
    return render(request, 'departments.html', context)


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()

    # # Deletes all projects with this criteria
    # Project.objects.filter(pk=2)\
    #     .delete()
    #
    # # Deletes all projects
    # Project.objects.all()\
    #     .delete()

    return redirect("info")
