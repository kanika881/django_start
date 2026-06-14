from django.db import models

class form_data(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    pwd=models.CharField()
    email=models.EmailField()

# Create your models here.
