# Generated by Django 5.2.2 on 2025-06-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner_url',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
