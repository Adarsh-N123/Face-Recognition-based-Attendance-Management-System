# Generated by Django 4.2 on 2023-05-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursenumber', models.CharField(max_length=20)),
                ('coursecode', models.CharField(max_length=50)),
                ('instructorname', models.CharField(max_length=50)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('totalclasses', models.CharField(max_length=10)),
                ('slots', models.CharField(max_length=50)),
            ],
        ),
    ]
