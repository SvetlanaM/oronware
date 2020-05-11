# Generated by Django 3.0.6 on 2020-05-05 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('herbs', '0005_remove_herb_ingredients'),
        ('main', '0004_delete_ingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Illness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Illness',
                'verbose_name_plural': 'Illnesses',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('note', models.TextField(blank=True)),
                ('preparing', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Recipe',
                'verbose_name_plural': 'Recipes',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='TemplateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, choices=[('kg', 'kilograms'), ('g', 'grams'), ('ks', 'pieces'), ('dg', 'dekagrams')], max_length=5)),
                ('value', models.PositiveIntegerField(blank=True)),
                ('herb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='herbs.Herb')),
                ('illness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Illness')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Recipe')),
            ],
            options={
                'verbose_name': 'Amount',
                'verbose_name_plural': 'Amounts',
                'abstract': False,
            },
        ),
    ]