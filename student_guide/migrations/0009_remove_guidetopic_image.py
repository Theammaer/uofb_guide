# Generated by Django 5.0.6 on 2024-09-28 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_guide', '0008_chapter_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guidetopic',
            name='image',
        ),
    ]
