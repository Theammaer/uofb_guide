# Generated by Django 5.0.6 on 2024-09-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_guide', '0006_alter_guidetopic_ar_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='ar_title',
            field=models.CharField(default='Arabic Title ', max_length=256, verbose_name='Arabic Title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='guidetopic',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='Guide Entry Image'),
        ),
    ]
