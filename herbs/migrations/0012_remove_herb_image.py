# Generated by Django 3.0.6 on 2020-05-18 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('herbs', '0011_auto_20200518_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='herb',
            name='image',
        ),
    ]
