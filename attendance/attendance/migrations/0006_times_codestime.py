# Generated by Django 4.2 on 2023-05-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='times',
            name='codestime',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
