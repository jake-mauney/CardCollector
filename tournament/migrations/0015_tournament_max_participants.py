# Generated by Django 5.1.2 on 2024-12-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0014_tournament_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='max_participants',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]