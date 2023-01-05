# Generated by Django 4.1.3 on 2022-12-01 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TWJTM', '0014_remove_usersdata_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='tmUsersData',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=80, null=True)),
                ('password', models.CharField(max_length=80, null=True)),
                ('emailid', models.EmailField(max_length=254, null=True)),
                ('mobile', models.CharField(max_length=50, null=True)),
                ('caption', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='UsersData',
        ),
    ]
