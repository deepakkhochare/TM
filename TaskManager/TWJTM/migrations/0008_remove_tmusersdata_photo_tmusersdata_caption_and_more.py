# Generated by Django 4.1.3 on 2022-12-01 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TWJTM', '0007_tmusersdata_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tmusersdata',
            name='photo',
        ),
        migrations.AddField(
            model_name='tmusersdata',
            name='caption',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tmusersdata',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
