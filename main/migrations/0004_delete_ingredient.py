# Generated by Django 3.0.6 on 2020-05-05 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20200505_1427'),
        ('main', '0003_auto_20200505_0835'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]
