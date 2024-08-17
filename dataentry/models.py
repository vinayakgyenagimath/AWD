from django.db import models

class Student(models.Model):
  roll_no = models.IntegerField()
  name=models.CharField(max_length=100)
  age=models.IntegerField()
  
  def __str__(self):
    return self.name
  
class Customer(models.Model):
  customer_name = models.CharField(max_length=10)
  country = models.CharField(max_length=10)
  
  def __str__(self):
    return self.country
# Create your models here.

class Employee(models.Model):
  employee_id = models.IntegerField()
  employee_name = models.CharField(max_length=50)
  designation = models.CharField(max_length=25)
  salary = models.DecimalField(max_digits=10 ,decimal_places=2)
  retirement =models.DecimalField(max_digits=10,decimal_places=2)
  other_benefits =models.DecimalField(max_digits=10,decimal_places=2)
  total_benefits = models.DecimalField(max_digits=10,decimal_places=2)
  total_compensation =models.DecimalField(max_digits=10,decimal_places=2)
  
  def __str__(self):
    return f'Employee Name {self.employee_name} and designation {self.designation}'
