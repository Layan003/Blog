# Generated by Django 5.1.2 on 2024-11-01 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='text',
        ),
    ]
