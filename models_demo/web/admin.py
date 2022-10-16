from django.contrib import admin
from models_demo.web.models import Employee, NullBlankDemo, Department, Project

# web/admin.py
# Register your models here.

"""
регистрираме класа Employee тук за да може да го видим в админ панела 
т.е. го връзва към администрацията чрез новият клас EmployeeAdmin
и чрез декоратора admin.register.
"""
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(NullBlankDemo)
class NullBlankDemoAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass