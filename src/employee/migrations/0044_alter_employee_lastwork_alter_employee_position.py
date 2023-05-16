# Generated by Django 4.2.1 on 2023-05-16 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0043_remove_employee_address_remove_employee_region_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='lastwork',
            field=models.CharField(blank=True, max_length=125, null=True, verbose_name='Последнее место работы'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(blank=True, help_text='Занимаемая должность на последнем месте работы?', max_length=255, null=True, verbose_name='Занимаемая должность'),
        ),
    ]
