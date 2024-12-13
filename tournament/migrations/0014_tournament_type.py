# Generated by Django 5.1.2 on 2024-12-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0013_alter_tournament_runner'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='type',
            field=models.CharField(choices=[('RCQ', 'RCQ'), ('SWISS', 'Swiss'), ('SINGLEELIM', 'Single Elimination'), ('ROBIN', 'Round Robin')], default='SWISS', max_length=200),
            preserve_default=False,
        ),
    ]
