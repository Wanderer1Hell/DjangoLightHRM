# Generated by Django 4.2.1 on 2023-06-09 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0024_sickleave_mrot'),
    ]

    operations = [
        migrations.AddField(
            model_name='sickleave',
            name='payment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='Выплата'),
        ),
    ]
