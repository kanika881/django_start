from django.db import models

class profile(models.Model):
    name=models.CharField(max_length=70)
    roll=models.CharField(max_length=60)
    city=models.CharField(max_length=80)
    email=models.EmailField(max_length=255)
    def __str__(self):
        return self.name


# Create your models here.
