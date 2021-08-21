from django.db import models

# Create your models here.
class Library(models.Model):
    ecode=models.CharField(max_length=50,default='')
    lname=models.CharField(max_length=50,default='')
    address=models.CharField(max_length=50,default='')
    mob=models.CharField(max_length=50,default='')
    usern=models.CharField(max_length=50,default='')
    pw=models.CharField(max_length=50,default='')

#{"ecode":"","lname":"","address":"","mob":"","usern":"","pw":""}
