# Generated by Django 3.0.6 on 2020-05-05 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('herbs', '0005_remove_herb_ingredients'),
        ('illnesses', '0003_auto_20200505_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='illness',
            name='herbs',
        ),
        migrations.RemoveField(
            model_name='illness',
            name='name',
        ),
        migrations.RemoveField(
            model_name='illness',
            name='value',
        ),
        migrations.CreateModel(
            name='IllnessModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, choices=[('kg', 'kilograms'), ('g', 'grams'), ('ks', 'pieces'), ('dg', 'dekagrams')], max_length=5)),
                ('value', models.PositiveIntegerField(blank=True)),
                ('herb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='herbs.Herb')),
                ('illness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='illnesses.Illness')),
            ],
            options={
                'verbose_name': 'Amount',
                'verbose_name_plural': 'Amounts',
                'abstract': False,
            },
        ),
    ]
