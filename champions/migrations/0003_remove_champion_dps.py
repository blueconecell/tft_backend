# Generated by Django 5.0.3 on 2024-03-05 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('champions', '0002_champion_job_champion_origin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champion',
            name='DPS',
        ),
    ]
