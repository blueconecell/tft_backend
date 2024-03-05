# Generated by Django 5.0.3 on 2024-03-05 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='계열 명', max_length=100)),
                ('job_description', models.TextField()),
                ('job_effect', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='계열 명', max_length=100)),
                ('origin_description', models.TextField()),
                ('origin_effect', models.TextField()),
            ],
        ),
    ]