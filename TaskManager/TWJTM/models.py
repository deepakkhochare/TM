#import filepath as filepath
from django.db import models
import mysql.connector

# Create your models here.
class tmUsersData(models.Model):
    userid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=80,null=True)
    password=models.CharField(max_length=80,null=True)
    emailid=models.EmailField(null=True)
    mobile=models.CharField(max_length=50,null=True)
    company=models.CharField(max_length=50,null=True)
    caption = models.CharField(max_length=200,null=True)
    image=models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.image

class taskData(models.Model):
    location=models.CharField(max_length=80)
    task=models.CharField(max_length=80)
    desc=models.CharField(max_length=200)
    start_date=models.DateField()
    estimated_date=models.DateField()
    end_date=models.DateField()
    comments=models.CharField(max_length=200)
    username=models.CharField(max_length=80,null=True)
    company=models.CharField(max_length=80)

    def __str__(self):
        return self.task


