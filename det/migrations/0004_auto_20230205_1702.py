# Generated by Django 3.2.15 on 2023-02-05 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('det', '0003_alter_user_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='designation',
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='profile/user.png', upload_to='profile/'),
        ),
    ]
