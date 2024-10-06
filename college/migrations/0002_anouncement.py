# Generated by Django 5.0.6 on 2024-08-18 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anouncement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(verbose_name='Puplish Date')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.college', verbose_name='College')),
            ],
        ),
    ]
