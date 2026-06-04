from django.db import models
class profile(models.Model):
    name=models.CharField(max_length=75)
    Email=models.EmailField(max_length=255)
    city=models.CharField(max_length=80)
    Phone=models.PositiveIntegerField()
    
# Create your models here.
