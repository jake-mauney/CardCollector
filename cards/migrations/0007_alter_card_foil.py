# Generated by Django 5.1.2 on 2024-12-12 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_alter_card_set_code_alter_card_set_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='foil',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
