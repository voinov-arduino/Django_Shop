# Generated by Django 4.0.4 on 2022-04-15 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_task_cena'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='cena',
        ),
    ]
