# Generated by Django 4.1.1 on 2023-01-16 05:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("scientific_conference", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Comment", new_name="Review",),
    ]
