from django.db import models

# Create your models here.
'''
Employee.objects.all()      # Select *
Employee.objects.create()   # Insert
Employee.objects.filter()   # Select + Where
Employee.objects.update()   # Update
Employee.objects.raw()      # raw SQL
'''


class Employee(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)

    # int > 0
    years_of_exp = models.PositiveIntegerField()
    # Text
    review = models.TextField()
    # Char field with included validator for emails
    email = models.EmailField()
    # Boolean field (True/False)
    works_full_time = models.BooleanField()
    job_level = models.CharField(max_length=20)
    photo = models.URLField()
    # Date field
    start_date = models.DateField()
    # Date/Time field
    birth_date = models.DateField()
    # Automatically filled upon creation of an Employee
    created_on = models.DateTimeField(auto_now=True)
    # Automatically filled on any update of the specific employee
    updated_on = models.DateTimeField(auto_now_add=True)

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        # return f"ID: {self.pk}; Name: {self.first_name} {self.last_name}"
        return f"ID: {self.pk}; Name: {self.fullname}"