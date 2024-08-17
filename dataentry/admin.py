from django.contrib import admin
from .models import Student,Customer,Employee

class EmployeeAdmin(admin.ModelAdmin):
  list_display = ['employee_id' ,'salary']

admin.site.register(Student)
admin.site.register(Customer)

admin.site.register(Employee)


# Register your models here.
