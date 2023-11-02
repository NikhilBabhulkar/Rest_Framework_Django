from django.db import models

# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=100)
    type=models.CharField(max_length=100,choices=(('CS','CS'),('IT','IT')))
    time=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
