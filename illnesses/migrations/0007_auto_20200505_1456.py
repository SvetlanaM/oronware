# Generated by Django 3.0.6 on 2020-05-05 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('illnesses', '0006_remove_illness_preparing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='illnessmodel',
            name='herb',
        ),
        migrations.RemoveField(
            model_name='illnessmodel',
            name='illness',
        ),
        migrations.DeleteModel(
            name='Illness',
        ),
        migrations.DeleteModel(
            name='IllnessModel',
        ),
    ]
