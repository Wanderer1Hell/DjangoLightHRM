# Generated by Django 4.2.1 on 2023-05-15 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0005_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='defaultdays',
            field=models.PositiveIntegerField(blank=True, default=30, null=True, verbose_name='Количество дней отпуска в год счетчик'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='enddate',
            field=models.DateField(null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='reason',
            field=models.CharField(blank=True, help_text='Добавить дополнительную информацию для отпуска', max_length=255, null=True, verbose_name='Причина отпуска'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='startdate',
            field=models.DateField(null=True, verbose_name='Дата начала'),
        ),
    ]