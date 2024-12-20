# Generated by Django 5.1.2 on 2024-12-12 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardImport', '0004_alter_importrequest_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importrequest',
            name='error_msg',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='importrequest',
            name='status',
            field=models.CharField(blank=True, choices=[('NEW', 'new'), ('IN PROCESS', 'In Process'), ('DONE', 'Done'), ('ERROR', 'Error')], max_length=10, null=True),
        ),
    ]
