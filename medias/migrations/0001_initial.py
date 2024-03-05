# Generated by Django 5.0.3 on 2024-03-05 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('augments', '0003_alter_augment_augment_tier'),
        ('champions', '0008_remove_champion_job_remove_champion_origin_and_more'),
        ('items', '0001_initial'),
        ('synergies', '0002_alter_job_name_alter_origin_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.URLField()),
                ('description', models.TextField()),
                ('augment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='augments.augment')),
                ('champion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='champions.champion')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='items.item')),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='synergies.job')),
                ('origin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='synergies.origin')),
            ],
        ),
    ]
