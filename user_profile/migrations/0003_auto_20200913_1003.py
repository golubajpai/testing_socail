# Generated by Django 3.1.1 on 2020-09-13 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20200913_0905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='user_profile',
            new_name='user',
        ),
    ]
