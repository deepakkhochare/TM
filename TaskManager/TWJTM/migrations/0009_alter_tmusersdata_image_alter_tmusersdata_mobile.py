# Generated by Django 4.1.3 on 2022-12-01 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TWJTM', '0008_remove_tmusersdata_photo_tmusersdata_caption_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmusersdata',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='tmusersdata',
            name='mobile',
            field=models.CharField(max_length=50),
        ),
    ]