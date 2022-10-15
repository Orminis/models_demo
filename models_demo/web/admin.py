from django.contrib import admin
from models_demo.web.models import Employee


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
