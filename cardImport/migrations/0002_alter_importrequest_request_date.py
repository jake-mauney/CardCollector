# Generated by Django 5.1.3 on 2024-12-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cardImport", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="importrequest",
            name="request_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
