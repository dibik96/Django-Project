# Generated by Django 5.1.4 on 2025-02-20 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
