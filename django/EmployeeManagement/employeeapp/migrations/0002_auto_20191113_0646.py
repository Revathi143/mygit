# Generated by Django 2.2.7 on 2019-11-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemanagement',
            name='contactNo',
            field=models.CharField(max_length=10),
        ),
    ]
