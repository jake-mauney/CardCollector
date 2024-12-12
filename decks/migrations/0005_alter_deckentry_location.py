# Generated by Django 5.1.2 on 2024-12-12 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0004_alter_deck_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deckentry',
            name='location',
            field=models.CharField(choices=[('MAIN', 'Mainboard'), ('SIDE', 'Sideboard')], max_length=20),
        ),
    ]