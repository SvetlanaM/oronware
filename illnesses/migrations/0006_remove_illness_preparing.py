# Generated by Django 3.0.6 on 2020-05-05 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('illnesses', '0005_auto_20200505_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='illness',
            name='preparing',
        ),
    ]