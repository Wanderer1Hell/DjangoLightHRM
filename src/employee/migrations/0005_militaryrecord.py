# Generated by Django 4.2.1 on 2023-05-24 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employee_is_terminated'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilitaryRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_military_service', models.BooleanField(default=False, verbose_name='Военнообязанный')),
                ('category', models.CharField(choices=[('военнообязанный', 'Военнообязанный'), ('запас', 'Запас'), ('не годный к службе', 'Не годный к службе'), ('подлежит призыву на ВС', 'Подлежит призыву на ВС')], max_length=50, verbose_name='Категория военного учета')),
                ('military_ticket_number', models.CharField(max_length=50, verbose_name='Номер военного билета')),
                ('issue_date', models.DateField(verbose_name='Дата выдачи')),
                ('reserve_category', models.CharField(choices=[('', ''), ('подлежит призыву на ВС', 'Подлежит призыву на ВС')], max_length=50, verbose_name='Категория запаса')),
                ('military_rank', models.CharField(choices=[('рядовой', 'Рядовой'), ('ефрейтор', 'Ефрейтор'), ('младший сержант', 'Младший сержант'), ('сержант', 'Сержант'), ('старший сержант', 'Старший сержант')], max_length=50, verbose_name='Военное звание')),
                ('composition', models.CharField(choices=[('офицеры', 'Офицеры'), ('прапорщики и мичманы', 'Прапорщики и мичманы'), ('сержанты и старшины', 'Сержанты и старшины'), ('солдаты и матросы', 'Солдаты и матросы')], max_length=50, verbose_name='Состав')),
                ('code', models.CharField(max_length=150, verbose_name='Полное кодовое обозначение ВУС')),
                ('vk_name', models.CharField(max_length=50, verbose_name='Наименование ВК')),
                ('demobilization_mark', models.CharField(max_length=150, verbose_name='Отметка о снятии с ВУ')),
                ('booking', models.BooleanField(default=False, verbose_name='Бронирование')),
                ('mobilization_certificate', models.CharField(max_length=150, verbose_name='Мобилизационный талон')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Сотрудник')),
            ],
        ),
    ]