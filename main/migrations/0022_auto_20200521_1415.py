# Generated by Django 2.2.12 on 2020-05-21 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_effect_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='substance',
            name='percentage',
        ),
        migrations.AddField(
            model_name='contraindication',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='effect',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='study_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='study_images', to='main.Study', verbose_name='study_image'),
        ),
        migrations.AlterField(
            model_name='effect',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='note'),
        ),
    ]
