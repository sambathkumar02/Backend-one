from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.TextField()
    email=models.EmailField()
    password=models.TextField()