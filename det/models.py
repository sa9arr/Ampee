from django.db import models
class User(models.Model):
    username=models.CharField(max_length=100, unique=True,)
    password=models.CharField(max_length=100, null=True)
    password2=models.CharField(max_length=100, null=True)
    fname=models.CharField(max_length=100, null=True)
    lname=models.CharField(max_length=100, null=True)
    email=models.CharField(max_length=100, null=True)
# Create your models here.
class Employee(models.Model):
 emname=models.CharField(max_length=100)
 ememail=models.EmailField(max_length=100)
 salary=models.BigIntegerField(null=True) 
 designation=models.CharField(max_length=100)
 photo=models.ImageField(upload_to='profile/',default='profile/user.png')
 