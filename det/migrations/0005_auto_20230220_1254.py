# Generated by Django 3.2.15 on 2023-02-20 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('det', '0004_auto_20230205_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='ememail',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='emname',
        ),
    ]
