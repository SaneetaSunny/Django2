# Generated by Django 3.0 on 2020-01-14 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_leave'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='Batch',
            field=models.CharField(default='JSD2', max_length=10),
        ),
    ]