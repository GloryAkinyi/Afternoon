# Generated by Django 4.2.7 on 2023-11-14 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0019_imagemodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='price',
            field=models.CharField(default='8000', max_length=50),
        ),
    ]
