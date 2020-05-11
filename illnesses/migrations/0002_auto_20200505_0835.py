# Generated by Django 3.0.6 on 2020-05-05 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('illnesses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='illness',
            old_name='pieces',
            new_name='value',
        ),
        migrations.RemoveField(
            model_name='illness',
            name='amount',
        ),
        migrations.AddField(
            model_name='illness',
            name='name',
            field=models.CharField(blank=True, choices=[('kg', 'kilograms'), ('g', 'grams'), ('ks', 'pieces'), ('dg', 'dekagrams')], max_length=5),
        ),
        migrations.AlterField(
            model_name='illness',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
