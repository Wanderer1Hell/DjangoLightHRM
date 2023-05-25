# Generated by Django 4.2.1 on 2023-05-25 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_militaryrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='militaryrecord',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано'),
        ),
        migrations.AddField(
            model_name='militaryrecord',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено'),
        ),
    ]
