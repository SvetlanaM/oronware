# Generated by Django 3.0.6 on 2020-05-05 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('illnesses', '0004_auto_20200505_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='illness',
            name='image',
        ),
        migrations.AlterField(
            model_name='illness',
            name='note',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='illness',
            name='preparing',
            field=models.TextField(blank=True),
        ),
    ]