# Generated by Django 5.0.6 on 2024-06-02 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_guide', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guidetopic',
            name='unit',
        ),
    ]
