# Generated by Django 3.0.6 on 2020-05-05 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbs', '0005_remove_herb_ingredients'),
        ('main', '0003_auto_20200505_0835'),
        ('recipes', '0002_auto_20200505_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='main.Ingredient', verbose_name='ingredients'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='herbs',
            field=models.ManyToManyField(blank=True, related_name='recipes', to='herbs.Herb', verbose_name='herbs'),
        ),
    ]
