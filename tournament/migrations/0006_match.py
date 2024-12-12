# Generated by Django 5.1.2 on 2024-12-04 02:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playerprofile', '0001_initial'),
        ('tournament', '0005_registration_tournament'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Player1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='playerprofile.player')),
            ],
        ),
    ]
