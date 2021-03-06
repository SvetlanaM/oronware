# Generated by Django 3.0.6 on 2020-05-18 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_study'),
        ('herbs', '0009_auto_20200518_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='herb',
            name='planting',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='herb',
            name='studies',
            field=models.ManyToManyField(blank=True, null=True, related_name='studies', to='main.Study', verbose_name='studies'),
        ),
    ]
