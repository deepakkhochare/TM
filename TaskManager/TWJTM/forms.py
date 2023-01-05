from django import forms
from .models import tmUsersData,taskData

from django.db import models
from django.forms import fields


class tmUsersForm(forms.ModelForm):
    class Meta:
        model = tmUsersData
        fields = [
            'username',
            'password',
            'emailid',
            'mobile',
            'caption',
            'company',
            'image',
        ]
    labels = {
        'username': 'User Name',
        'password':'Password',
        'emailid':'Email Id',
        'mobile':'Mobile No',
        'caption':'Photo Name',
        'company':'Company',
        'image':'Photo',
    }

class taskForm(forms.ModelForm):
    class Meta:
        model = taskData
        fields = [
            'location',
            'task',
            'desc',
            'start_date',
            'estimated_date',
            'end_date',
            'comments',
            'username',
            'company',

        ]

    labels = {
        'location':'Location',
        'task':'Task',
        'desc':'Description',
        'start_date':'Starting Date',
        'estimated_date':'Estimated Completion Date',
        'end_date':'Actual Completion Date',
        'comments':'Comments',
        'username':'Username',
        'company':'Company',
    }

