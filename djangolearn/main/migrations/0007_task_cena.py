# Generated by Django 4.0.4 on 2022-04-15 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_task_cena'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='cena',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='Цена'),
        ),
    ]