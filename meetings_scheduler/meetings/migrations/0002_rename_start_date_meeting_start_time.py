# Generated by Django 5.0.6 on 2024-06-12 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='start_date',
            new_name='start_time',
        ),
    ]
