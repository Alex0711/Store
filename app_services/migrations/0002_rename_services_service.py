# Generated by Django 4.0.2 on 2022-02-22 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
    ]
