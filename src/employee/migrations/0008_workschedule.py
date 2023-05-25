# Generated by Django 4.2.1 on 2023-05-25 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_bank_work_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateField(verbose_name='Месяц')),
                ('schedule', models.TextField(verbose_name='Расписание')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Work Schedule',
                'verbose_name_plural': 'Work Schedules',
                'ordering': ['-month'],
            },
        ),
    ]