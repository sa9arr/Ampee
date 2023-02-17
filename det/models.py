from django.db import models

# Create your models here.
class User(models.Model):
 name=models.CharField(max_length=100)
 email=models.EmailField(max_length=100)
 designation=models.CharField(max_length=100)
 photo=models.ImageField(upload_to='profile/',default='profile/user.png')
 