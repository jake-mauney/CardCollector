# Generated by Django 5.1.2 on 2024-12-12 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_card_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='set_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='set_num',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
