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
