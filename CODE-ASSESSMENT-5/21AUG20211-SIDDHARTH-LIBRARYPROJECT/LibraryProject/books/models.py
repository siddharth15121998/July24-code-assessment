from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=50,default='')
    author=models.CharField(max_length=50,default='')
    descp=models.CharField(max_length=50,default='')
    publisher=models.CharField(max_length=50,default='')
    price=models.CharField(max_length=50,default='')

#{"name":"","author":"","descp":"","publisher":"","price":""}
