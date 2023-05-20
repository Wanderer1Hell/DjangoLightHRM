# Generated by Django 4.2.1 on 2023-05-20 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование организации')),
                ('leader_lastname', models.CharField(max_length=100, verbose_name='Фамилия руководителя')),
                ('leader_name', models.CharField(max_length=100, verbose_name='Имя руководителя')),
                ('leader_namemiddle', models.CharField(max_length=100, verbose_name='Отчество руководителя')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('description', models.CharField(blank=True, max_length=125, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
                'ordering': ['name', 'created'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=125, verbose_name='Фамилия')),
                ('firstname', models.CharField(max_length=125, verbose_name='Имя')),
                ('othername', models.CharField(blank=True, max_length=125, null=True, verbose_name='Отчество')),
                ('sex', models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], default='Мужской', max_length=10, verbose_name='Пол')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('hometown', models.CharField(blank=True, max_length=125, null=True, verbose_name='Место рождения')),
                ('title', models.CharField(choices=[('Военный билет', 'Военный билет'), ('Паспорт', 'Паспорт'), ('Свидетельство о рождении', 'Свидетельство о рождении')], default='Паспорт', max_length=24, null=True, verbose_name='Вид документа')),
                ('Document_series', models.CharField(blank=True, max_length=15, null=True, verbose_name='Серия документа')),
                ('Document_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер документа')),
                ('Date_issue', models.DateField(null=True, verbose_name='Дата выдачи (YYYY-mm-dd)')),
                ('Issued', models.CharField(blank=True, max_length=125, null=True, verbose_name='Кем выдан')),
                ('Unit_code', models.CharField(blank=True, max_length=15, null=True, verbose_name='Код подразделения ')),
                ('Date_Registrations', models.DateField(null=True, verbose_name='Дата регистрации')),
                ('Zip_Code', models.CharField(blank=True, max_length=15, null=True, verbose_name='Почтовый индекс ')),
                ('Region', models.CharField(blank=True, max_length=125, null=True, verbose_name='Область')),
                ('District', models.CharField(blank=True, max_length=125, null=True, verbose_name='Район')),
                ('Settlement', models.CharField(blank=True, max_length=125, null=True, verbose_name='Населенный пункт')),
                ('Street', models.CharField(blank=True, max_length=125, null=True, verbose_name='Улица')),
                ('Home', models.CharField(blank=True, max_length=125, null=True, verbose_name='Дом')),
                ('Corps', models.CharField(blank=True, max_length=125, null=True, verbose_name='Корпус')),
                ('Apartment', models.CharField(blank=True, max_length=125, null=True, verbose_name='Квартира')),
                ('residence', models.CharField(max_length=125, verbose_name='Текущее место жительства')),
                ('Resolution', models.CharField(blank=True, help_text='Разрешение на работу иностранного сотрудника', max_length=125, null=True, verbose_name='Разрешение на работу №')),
                ('ssnitnumber', models.CharField(blank=True, max_length=30, null=True, verbose_name='СНИЛС')),
                ('tinnumber', models.CharField(blank=True, max_length=15, null=True, verbose_name='ИНН')),
                ('tel', phonenumber_field.modelfields.PhoneNumberField(default='+79', help_text='Введите номер с кодом страны', max_length=128, region=None, verbose_name='Номер телефона')),
                ('email', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Email')),
                ('education', models.CharField(choices=[('Начальное профессиональное образование', 'Основное общее образование'), ('Неполное высшее образование', 'Среднее общее образование'), ('Среднее профессиональное образование', 'Среднее профессиональное образование'), ('Основное общее образование', 'Высшее образование'), ('Начальное (общее) образование', 'Начальное общее образование'), ('Послевузовское образование', 'Другое')], default='Начальное профессиональное образование', help_text='Уровень образования', max_length=38, null=True, verbose_name='Образование')),
                ('lastwork', models.CharField(blank=True, max_length=125, null=True, verbose_name='Последнее место работы')),
                ('position', models.CharField(blank=True, help_text='Занимаемая должность на последнем месте работы?', max_length=255, null=True, verbose_name='Занимаемая должность')),
                ('startdate', models.DateField(help_text='Дата по приказу', null=True, verbose_name='Дата приема на работу')),
                ('employeetype', models.CharField(choices=[('Полный рабочий день', 'Полный рабочий день'), ('Неполный рабочий день', 'Неполный рабочий день'), ('Договор', 'Договор'), ('Стажер', 'Стажер')], default='Полный рабочий день', max_length=21, null=True, verbose_name='Тип сотрудника')),
                ('employeeid', models.CharField(blank=True, max_length=10, null=True, verbose_name='Табельный номер сотрудника')),
                ('dateissued', models.DateField(help_text='Дата выдачи пропуска', null=True, verbose_name='Дата выдачи пропуска')),
                ('image', models.FileField(blank=True, default='default.png', help_text='Загрузи изображения не более 2.0 Мб', null=True, upload_to='profiles', verbose_name='Изображение профиля')),
                ('bio', models.CharField(blank=True, default='', help_text='Дополнительная информация', max_length=255, null=True, verbose_name='Заметки')),
                ('is_blocked', models.BooleanField(default=False, help_text='button to toggle employee block and unblock', verbose_name='Is Blocked')),
                ('is_deleted', models.BooleanField(default=False, help_text='button to toggle employee deleted and undelete', verbose_name='Is Deleted')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Созданно')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')),
                ('department', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.department', verbose_name='Департамент')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('flag', models.ImageField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Nationality',
                'verbose_name_plural': 'Nationality',
                'ordering': ['name', 'created'],
            },
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('description', models.CharField(blank=True, max_length=125, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Religion',
                'verbose_name_plural': 'Religions',
                'ordering': ['name', 'created'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('description', models.CharField(blank=True, max_length=125, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
                'ordering': ['name', 'created'],
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Состоит в зарегистрированном браке', 'В браке'), ('Никогда не состоял(не состояла) в браке', 'Одинок(а)'), ('В разводе', 'В разводе'), ('Вдова', 'Вдова'), ('Вдовец', 'Вдовец')], default='Никогда не состоял(не состояла) в браке', max_length=40, null=True, verbose_name='Семейное положение')),
                ('spouse', models.CharField(blank=True, max_length=255, null=True, verbose_name='Супруг\\а (ФИО)')),
                ('occupation', models.CharField(blank=True, help_text='род занятий супруга\\ги', max_length=125, null=True, verbose_name='Профессия')),
                ('tel', phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, help_text='Введите номер с кодом страны', max_length=128, null=True, region=None, verbose_name='Номер телефона супруга\\ги')),
                ('children', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Кол-во детей')),
                ('nextofkin', models.CharField(help_text='ФИО', max_length=255, null=True, verbose_name='Ближайший родственник')),
                ('relationship', models.CharField(choices=[('Отец', 'Отец'), ('Мать', 'Мать'), ('Сестра', 'Сестра'), ('Брат', 'Брат'), ('Дядя', 'Дядя'), ('Тётя', 'Тетя'), ('Муж', 'Муж'), ('Жена', 'Жена'), ('Жених', 'Жених'), ('Cousin', 'Cousin'), ('Жена', 'Невеста'), ('Племянница', 'Племянница'), ('Племянник', 'Племянник'), ('Сын', 'Сын'), ('Дочь', 'Дочь')], help_text='Кем для вас является этот человек?', max_length=40, null=True, verbose_name='Родственные связи ')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Relationship',
                'verbose_name_plural': 'Relationships',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField(null=True, verbose_name='Дата начала')),
                ('enddate', models.DateField(null=True, verbose_name='Дата окончания')),
                ('leavetype', models.CharField(choices=[('sick', 'ежегодный основной оплачиваемый отпуск'), ('casual', 'ежегодный дополнительный оплачиваемый отпуск'), ('emergency', 'отпуск без сохранения заработной платы'), ('study', 'учебный отпуск'), ('birth', 'отпуск по беременности и родам'), ('other', 'другой')], default='sick', max_length=25, null=True, verbose_name='Тип отпуска')),
                ('reason', models.CharField(blank=True, help_text='Добавить дополнительную информацию для отпуска', max_length=255, null=True, verbose_name='Примечание')),
                ('defaultdays', models.PositiveIntegerField(blank=True, default=140, null=True, verbose_name='Количество дней отпуска в год счетчик')),
                ('status', models.CharField(default='pending', max_length=12)),
                ('is_approved', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Leave',
                'verbose_name_plural': 'Leaves',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='nationality',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.nationality', verbose_name='Национальность'),
        ),
        migrations.AddField(
            model_name='employee',
            name='religion',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.religion', verbose_name='Гражданство'),
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.role', verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(help_text='С кем мы должны связаться?', max_length=255, null=True, verbose_name='ФИО')),
                ('tel', phonenumber_field.modelfields.PhoneNumberField(default='+79', help_text='Введите номер с кодом страны', max_length=128, region=None, verbose_name='Номер телефона')),
                ('location', models.CharField(max_length=125, null=True, verbose_name='Место жительства')),
                ('relationship', models.CharField(choices=[('Отец', 'Отец'), ('Мать', 'Мать'), ('Сестра', 'Сестра'), ('Брат', 'Брат'), ('Дядя', 'Дядя'), ('Тетя', 'Тетя'), ('Муж', 'Муж'), ('Жена', 'Жена'), ('Сын', 'Сын'), ('Дочь', 'Дочь')], default='Отец', help_text='Кто этот человек для вас?', max_length=40, null=True, verbose_name='Отношения с человеком')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Emergency',
                'verbose_name_plural': 'Emergency',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_file', models.FileField(upload_to='documents/%Y/%m/%d/', verbose_name='Файл документа')),
                ('filename', models.CharField(max_length=255, verbose_name='Название файла')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='employee.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, null=True, verbose_name='Наименование банка')),
                ('account', models.CharField(help_text='Номер счета сотрудника', max_length=30, null=True, verbose_name='Номер счета')),
                ('branch', models.CharField(blank=True, help_text='В каком отделении был открыт счет', max_length=125, null=True, verbose_name='Филиал')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=16, null=True, verbose_name='Оклад')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')),
                ('employee', models.ForeignKey(help_text='Выберите сотрудника(ов) для добавления банковского счета', null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Bank',
                'verbose_name_plural': 'Banks',
                'ordering': ['-name', '-account'],
            },
        ),
    ]
