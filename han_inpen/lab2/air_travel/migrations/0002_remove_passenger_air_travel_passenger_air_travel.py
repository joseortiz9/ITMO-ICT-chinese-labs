# Generated by Django 4.1.1 on 2023-01-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("air_travel", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="passenger", name="Air_travel",),
        migrations.AddField(
            model_name="passenger",
            name="air_travel",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
