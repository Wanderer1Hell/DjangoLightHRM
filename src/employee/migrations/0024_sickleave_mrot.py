# Generated by Django 4.2.1 on 2023-06-09 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0023_sickleave'),
    ]

    operations = [
        migrations.AddField(
            model_name='sickleave',
            name='mrot',
            field=models.DecimalField(decimal_places=2, max_digits=16, null=True, verbose_name='МРОТ'),
        ),
    ]
