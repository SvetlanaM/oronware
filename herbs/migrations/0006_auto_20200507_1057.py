# Generated by Django 3.0.6 on 2020-05-07 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbs', '0005_remove_herb_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herb',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Herb'),
        ),
    ]
