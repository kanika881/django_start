from django.db import models

class reg_model(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    pwd=models.CharField()
    cpwd=models.CharField()

# Create your models here.
