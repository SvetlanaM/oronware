# Generated by Django 3.0.6 on 2020-05-18 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200518_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='illness',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='illness',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
