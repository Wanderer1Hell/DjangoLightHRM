# Generated by Django 4.2.1 on 2023-05-25 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_workschedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата праздника')),
            ],
            options={
                'verbose_name': 'Праздник',
                'verbose_name_plural': 'Праздники',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateField(verbose_name='Месяц')),
                ('work_hours', models.IntegerField(verbose_name='Часы работы в день')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'График работы',
                'verbose_name_plural': 'Графики работы',
            },
        ),
    ]
