# Generated by Django 3.2.15 on 2023-03-14 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('det', '0004_employee_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.BigIntegerField(null=True),
        ),
    ]
