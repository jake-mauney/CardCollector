# Generated by Django 5.1.2 on 2024-12-10 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteutils', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_items',
            name='login_logout',
            field=models.CharField(choices=[('LOGIN', 'Login'), ('LOGOUT', 'Logout')], default=1, max_length=200),
            preserve_default=False,
        ),
    ]
