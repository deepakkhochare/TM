# Generated by Django 4.1.3 on 2022-11-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TWJTM', '0002_alter_tmusersdata_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmusersdata',
            name='userid',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
