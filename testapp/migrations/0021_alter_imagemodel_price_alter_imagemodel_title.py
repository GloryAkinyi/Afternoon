# Generated by Django 4.2.7 on 2023-11-14 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0020_imagemodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
