# Generated by Django 4.1.3 on 2022-11-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TWJTM', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmusersdata',
            name='userid',
            field=models.IntegerField(blank=True, default=None, primary_key=True, serialize=False),
        ),
    ]
