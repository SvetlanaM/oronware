# Generated by Django 2.2.12 on 2020-05-21 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20200519_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatemodel',
            name='name',
            field=models.CharField(blank=True, choices=[('kg', 'kilograms'), ('g', 'grams'), ('ks', 'pieces'), ('dg', 'dekagrams'), ('per', '%')], max_length=5, verbose_name='name'),
        ),
    ]
