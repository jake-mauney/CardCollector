# Generated by Django 5.1.3 on 2024-11-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("decks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="deckentry",
            name="location",
            field=models.CharField(
                choices=[("MAIN", "Mainboard"), ("SIDE", "Sidedeck")],
                default="MAIN",
                max_length=20,
            ),
            preserve_default=False,
        ),
    ]
