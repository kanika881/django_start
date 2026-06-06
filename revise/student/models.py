from django.db import models
class register_d(models.Model):
    name=models.CharField(max_length=77)
    user_id=models.CharField(max_length=75)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=255)

class Login(models.Model):
    user_id=models.CharField(max_length=75)
    password=models.CharField(max_length=20)
    
    
# Create your models here.
