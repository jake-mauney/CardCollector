# Generated by Django 5.1.2 on 2024-12-04 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_registration_deck'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='player',
        ),
    ]
