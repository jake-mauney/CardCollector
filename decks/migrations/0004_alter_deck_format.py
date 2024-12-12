# Generated by Django 5.1.2 on 2024-12-12 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0003_deck_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='format',
            field=models.CharField(blank=True, choices=[('STANDARD', 'Standard'), ('PIONEER', 'Pioneer'), ('PAUPER', 'Pauper'), ('MODERN', 'Modern')], max_length=10, null=True),
        ),
    ]