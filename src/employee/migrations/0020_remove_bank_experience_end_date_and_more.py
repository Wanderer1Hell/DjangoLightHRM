# Generated by Django 4.2.1 on 2023-06-03 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0019_bank_experience_end_date_bank_experience_start_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='experience_end_date',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='experience_start_date',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='position',
        ),
    ]
