from django.db import models


# Create your models here.

class Employee(models.Model):
    first_name


'''
Employee.objects.all()      # Select *
Employee.objects.create()   # Insert
Employee.objects.filter()   # Select + Where
Employee.objects.update()   # Update
Employee.objects.raw()      # raw SQL
'''
