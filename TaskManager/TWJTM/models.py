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

class InvData(models.Model):
    inv_id=models.IntegerField(primary_key=True)
    inv_name=models.CharField(max_length=80)
    inv_address=models.CharField(max_length=100)
    mobile=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    aadhar=models.CharField(max_length=20)
    pan=models.CharField(max_length=20)
    account_no=models.CharField(max_length=20)
    ifsc=models.CharField(max_length=15)
    bank_name=models.CharField(max_length=50)
    nominee_name=models.CharField(max_length=50)
    nominee_aadhar=models.CharField(max_length=50)
    aadhar_front=models.ImageField(upload_to='images/',null=True)
    aadhar_back=models.ImageField(upload_to='images/',null=True)
    pan_front=models.ImageField(upload_to='images/',null=True)
    nominee_aadhar_front=models.ImageField(upload_to='images/',null=True)
    reference_name=models.CharField(max_length=50)
    amount=models.FloatField()
    company=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.aadhar_front

