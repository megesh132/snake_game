from django.db import models
# Create your models here.
class register(models.Model):
    email=models.EmailField(primary_key=True, unique=True,max_length=30)
    fullname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

