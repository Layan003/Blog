# Generated by Django 5.1.2 on 2024-11-01 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_rename_post_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
