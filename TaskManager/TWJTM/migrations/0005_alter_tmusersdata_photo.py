# Generated by Django 4.1.3 on 2022-11-30 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TWJTM', '0004_tmusersdata_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmusersdata',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
