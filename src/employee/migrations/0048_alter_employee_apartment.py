# Generated by Django 4.2.1 on 2023-05-16 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0047_alter_employee_apartment_alter_employee_corps_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Apartment',
            field=models.CharField(blank=True, default='Кв.', max_length=125, null=True, verbose_name='Квартира'),
        ),
    ]
