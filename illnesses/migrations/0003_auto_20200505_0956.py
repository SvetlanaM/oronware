# Generated by Django 3.0.6 on 2020-05-05 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbs', '0005_remove_herb_ingredients'),
        ('illnesses', '0002_auto_20200505_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='illness',
            name='herbs',
            field=models.ManyToManyField(blank=True, related_name='illnesses', to='herbs.Herb', verbose_name='herbs'),
        ),
    ]
