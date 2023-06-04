import datetime
from calendar import calendar

from employee.utility import code_format
from django.db import models
from employee.managers import EmployeeManager, LeaveManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your models here.
class Role(models.Model):
    '''
        Role Table eg. Staff,Manager,H.R ...
    '''
    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125, null=True, blank=True)

    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)

    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')
        ordering = ['name', 'created']

    def __str__(self):
        return self.name


class Department(models.Model):
    '''
     Department Employee belongs to. eg. Transport, Engineering.
    '''
    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125, null=True, blank=True)

    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
        ordering = ['name', 'created']

    def __str__(self):
        return self.name


class Nationality(models.Model):
    name = models.CharField(max_length=125)
    flag = models.ImageField(null=True, blank=True)  # work on path

    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)

    class Meta:
        verbose_name = _('Nationality')
        verbose_name_plural = _('Nationality')
        ordering = ['name', 'created']

    def __str__(self):
        return self.name


class Religion(models.Model):
    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125, null=True, blank=True)

    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)

    class Meta:
        verbose_name = _('Religion')
        verbose_name_plural = _('Religions')
        ordering = ['name', 'created']

    def __str__(self):
        return self.name


class Bank(models.Model):
    WORK_SCHEDULE_CHOICES = [
        (1, '8 часов в день (40 в неделю)'),
        (2, '2,5 часа в день (четыре раза в неделю)'),
        (3, '2 дня рабочих 2 выходных'),
    ]

    employee = models.ForeignKey('employee', help_text='Выберите сотрудника(ов) для добавления банковского счета',
                                 on_delete=models.CASCADE, null=True, blank=False, verbose_name='Сотрудник')
    name = models.CharField(_('Наименование банка'), max_length=125, blank=False, null=True, help_text='')
    account = models.CharField(_('Номер счета'), help_text='Номер счета сотрудника', max_length=30, blank=False,
                               null=True)
    branch = models.CharField(_('Филиал'), help_text='В каком отделении был открыт счет', max_length=125, blank=True,
                              null=True)
    salary = models.DecimalField(_('Оклад'), max_digits=16, decimal_places=2, null=True, blank=False)
    work_schedule = models.IntegerField(_('График работы'), choices=WORK_SCHEDULE_CHOICES, null=True, blank=True)
    labor_book_series = models.CharField(_('Серия трудовой книжки'), max_length=10, null=True, blank=True)
    labor_book_number = models.CharField(_('Номер трудовой книжки'), max_length=10, null=True, blank=True)
    labor_book_issue_date = models.DateField(_('Дата выдачи трудовой книжки'), null=True, blank=True)
    labor_book_in_possession = models.BooleanField(_('Трудовая книжка на руках'), default=False)

    created = models.DateTimeField(verbose_name=_('Создано'), auto_now_add=True, null=True)
    updated = models.DateTimeField(verbose_name=_('Обновлено'), auto_now=True, null=True)

    class Meta:
        verbose_name = _('Bank')
        verbose_name_plural = _('Banks')
        ordering = ['-name', '-account']

    def __str__(self):
        return str(self.name)


class EmploymentHistory(models.Model):
    employee = models.ForeignKey('employee', on_delete=models.CASCADE)
    experience_start_date = models.DateField(_('Дата начала'), null=True, blank=True)
    experience_end_date = models.DateField(_('Дата окончания'), null=True, blank=True)
    position = models.CharField(_('Должность'), max_length=255, null=True, blank=True)
    organization = models.CharField(_('Организация'), max_length=255, null=True, blank=True)



class Emergency(models.Model):
    FATHER = 'Отец'
    MOTHER = 'Мать'
    SIS = 'Сестра'
    BRO = 'Брат'
    UNCLE = 'Дядя'
    AUNTY = 'Тетя'
    HUSBAND = 'Муж'
    WIFE = 'Жена'
    SON = 'Сын'
    DAUGHTER = 'Дочь'

    EMERGENCY_RELATIONSHIP = (
        (FATHER, 'Отец'),
        (MOTHER, 'Мать'),
        (SIS, 'Сестра'),
        (BRO, 'Брат'),
        (UNCLE, 'Дядя'),
        (AUNTY, 'Тетя'),
        (HUSBAND, 'Муж'),
        (WIFE, 'Жена'),
        (SON, 'Сын'),
        (DAUGHTER, 'Дочь'),
    )

    # access table: employee.emergency_set.
    employee = models.ForeignKey('employee', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Сотрудник')
    fullname = models.CharField(_('ФИО'), help_text='С кем мы должны связаться?', max_length=255, null=True,
                                blank=False)
    tel = PhoneNumberField(default='+79', null=False, blank=False, verbose_name='Номер телефона',
                           help_text='Введите номер с кодом страны')
    location = models.CharField(_('Место жительства'), max_length=125, null=True, blank=False)
    relationship = models.CharField(_('Отношения с человеком'), help_text='Кто этот человек для вас?', max_length=40,
                                    default=FATHER, choices=EMERGENCY_RELATIONSHIP, blank=False, null=True)

    created = models.DateTimeField(verbose_name=_('Создано'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Обновлено'), auto_now=True)

    class Meta:
        verbose_name = 'Emergency'
        verbose_name_plural = 'Emergency'
        ordering = ['-created']

    def __str__(self):
        return self.fullname

    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True, null=True)
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True, null=True)


class Relationship(models.Model):
    MARRIED = 'Состоит в зарегистрированном браке'
    SINGLE = 'Никогда не состоял(не состояла) в браке'
    DIVORCED = 'В разводе'
    WIDOW = 'Вдова'
    WIDOWER = 'Вдовец'

    STATUS = (
        (MARRIED, 'В браке'),
        (SINGLE, 'Одинок(а)'),
        (DIVORCED, 'В разводе'),
        (WIDOW, 'Вдова'),
        (WIDOWER, 'Вдовец'),
    )

    FATHER = 'Отец'
    MOTHER = 'Мать'
    SIS = 'Сестра'
    BRO = 'Брат'
    UNCLE = 'Дядя'
    AUNTY = 'Тётя'
    HUSBAND = 'Муж'
    WIFE = 'Жена'
    FIANCE = 'Жених'
    FIANCEE = 'Жена'
    COUSIN = 'Cousin'
    NIECE = 'Племянница'
    NEPHEW = 'Племянник'
    SON = 'Сын'
    DAUGHTER = 'Дочь'

    NEXTOFKIN_RELATIONSHIP = (
        (FATHER, 'Отец'),
        (MOTHER, 'Мать'),
        (SIS, 'Сестра'),
        (BRO, 'Брат'),
        (UNCLE, 'Дядя'),
        (AUNTY, 'Тетя'),
        (HUSBAND, 'Муж'),
        (WIFE, 'Жена'),
        (FIANCE, 'Жених'),
        (COUSIN, 'Cousin'),
        (FIANCEE, 'Невеста'),
        (NIECE, 'Племянница'),
        (NEPHEW, 'Племянник'),
        (SON, 'Сын'),
        (DAUGHTER, 'Дочь'),
    )

    # access table: employee.relationship_set.or related_name = 'relation' employee.relation.***
    employee = models.ForeignKey('employee', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Сотрудник')
    status = models.CharField(_('Семейное положение'), max_length=40, default=SINGLE, choices=STATUS, blank=False,
                              null=True)
    spouse = models.CharField(_('Супруг\а (ФИО)'), max_length=255, blank=True, null=True)
    occupation = models.CharField(_('Профессия'), max_length=125, help_text='род занятий супруга\ги', blank=True,
                                  null=True)
    tel = PhoneNumberField(default=None, null=True, blank=True, verbose_name='Номер телефона супруга\ги',
                           help_text='Введите номер с кодом страны')
    children = models.PositiveIntegerField(_('Кол-во детей'), null=True, blank=True, default=0)

    # recently added - 29/03/19
    nextofkin = models.CharField(_('Ближайший родственник'), max_length=255, blank=False, null=True,
                                 help_text='ФИО')
    relationship = models.CharField(_('Родственные связи '),
                                    help_text='Кем для вас является этот человек?', max_length=40,
                                    choices=NEXTOFKIN_RELATIONSHIP, blank=False, null=True)

    # close recent

    created = models.DateTimeField(verbose_name=_('Создано'), auto_now_add=True, null=True)
    updated = models.DateTimeField(verbose_name=_('Обновлено'), auto_now=True, null=True)

    class Meta:
        verbose_name = 'Relationship'
        verbose_name_plural = 'Relationships'
        ordering = ['created']

    def __str__(self):
        if self.status == 'Married':
            return self.spouse
        return self.status


class Employee(models.Model):
    MALE = 'Мужской'
    FEMALE = 'Женский'

    GENDER = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),

    )

    MILITARY = 'Военный билет'
    PASSPORT = 'Паспорт'
    СERTIFICATE = 'Свидетельство о рождении'

    TITLE = (
        (MILITARY, 'Военный билет'),
        (PASSPORT, 'Паспорт'),
        (СERTIFICATE, 'Свидетельство о рождении'),

    )

    FULL_TIME = 'Полный рабочий день'
    PART_TIME = 'Неполный рабочий день'
    CONTRACT = 'Договор'
    INTERN = 'Стажер'

    EMPLOYEETYPE = (
        (FULL_TIME, 'Полный рабочий день'),
        (PART_TIME, 'Неполный рабочий день'),
        (CONTRACT, 'Договор'),
        (INTERN, 'Стажер'),
    )

    OLEVEL = 'Начальное (общее) образование'
    SENIORHIGH = 'Начальное профессиональное образование'
    JUNIORHIGH = 'Неполное высшее образование'
    TERTIARY = 'Основное общее образование'
    PRIMARY = 'Среднее профессиональное образование'
    OTHER = 'Послевузовское образование'

    EDUCATIONAL_LEVEL = (
        (SENIORHIGH, 'Основное общее образование'),
        (JUNIORHIGH, 'Среднее общее образование'),
        (PRIMARY, 'Среднее профессиональное образование'),
        (TERTIARY, 'Высшее образование'),
        (OLEVEL, 'Начальное общее образование'),
        (OTHER, 'Другое'),
    )

    AHAFO = 'Ahafo'
    ASHANTI = 'Ashanti'
    BONOEAST = 'Bono East'
    BONO = 'Bono'
    CENTRAL = 'Central'
    EASTERN = 'Eastern'
    GREATER = 'Greater Accra'
    NORTHEAST = 'North East'
    NORTHERN = 'Northen'
    OTI = 'Oti'
    SAVANNAH = 'Savannah'
    UPPEREAST = 'Upper East'
    UPPERWEST = 'Upper West'
    VOLTA = 'Volta'
    WESTERNNORTH = 'Western North'
    WESTERN = 'Western'

    GHANA_REGIONS = (
        (AHAFO, 'Ahafo'),
        (ASHANTI, 'Ashanti'),
        (BONOEAST, 'Bono East'),
        (BONO, 'Bono'),
        (CENTRAL, 'Central'),
        (EASTERN, 'Eastern'),
        (GREATER, 'Greater Accra'),
        (NORTHEAST, 'Northen East'),
        (NORTHERN, 'Northen'),
        (OTI, 'Oti'),
        (SAVANNAH, 'Savannah'),
        (UPPEREAST, 'Upper East'),
        (UPPERWEST, 'Upper West'),
        (VOLTA, 'Volta'),
        (WESTERNNORTH, 'Western North'),
        (WESTERN, 'Western'),
    )

    # PERSONAL DATA
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    lastname = models.CharField(_('Фамилия'), max_length=125, null=False, blank=False)
    firstname = models.CharField(_('Имя'), max_length=125, null=False, blank=False)
    othername = models.CharField(_('Отчество'), max_length=125, null=True, blank=True)
    sex = models.CharField(_('Пол'), max_length=10, default=MALE, choices=GENDER, blank=False)
    birthday = models.DateField(_('Дата рождения'), blank=False, null=False)
    hometown = models.CharField(_('Место рождения'), max_length=125, null=True, blank=True)
    title = models.CharField(_('Вид документа'), max_length=24, default=PASSPORT, choices=TITLE, blank=False, null=True)
    Document_series = models.CharField(_('Серия документа'), max_length=15, null=True, blank=True)
    Document_number = models.CharField(_('Номер документа'), max_length=15, null=True, blank=True)
    Date_issue = models.DateField(_('Дата выдачи (YYYY-mm-dd)'), blank=False, null=True)
    Issued = models.CharField(_('Кем выдан'), max_length=125, null=True, blank=True)
    Unit_code = models.CharField(_('Код подразделения '), max_length=15, null=True, blank=True)
    Date_Registrations = models.DateField(_('Дата регистрации'), blank=False, null=True)
    Zip_Code = models.CharField(_('Почтовый индекс '), max_length=15, null=True, blank=True)
    Region = models.CharField(_('Область'), max_length=125, null=True, blank=True)
    District = models.CharField(_('Район'), max_length=125, null=True, blank=True)
    Settlement = models.CharField(_('Населенный пункт'), max_length=125, null=True, blank=True)
    Street = models.CharField(_('Улица'), max_length=125, null=True, blank=True)
    Home = models.CharField(_('Дом'), max_length=125, null=True, blank=True)
    Corps = models.CharField(_('Корпус'), max_length=125, null=True, blank=True)
    Apartment = models.CharField(_('Квартира'), max_length=125, null=True, blank=True)
    residence = models.CharField(_('Текущее место жительства'), max_length=125, null=False, blank=False)
    religion = models.ForeignKey(Religion, verbose_name=_('Гражданство'), on_delete=models.SET_NULL, null=True,
                                 default=None)
    nationality = models.ForeignKey(Nationality, verbose_name=_('Национальность'), on_delete=models.SET_NULL, null=True,
                                    default=None)
    Resolution = models.CharField(_('Разрешение на работу №'), help_text='Разрешение на работу иностранного сотрудника',
                                  max_length=125, null=True, blank=True)
    ssnitnumber = models.CharField(_('СНИЛС'), max_length=30, null=True, blank=True)
    tinnumber = models.CharField(_('ИНН'), max_length=15, null=True, blank=True)
    tel = PhoneNumberField(default='+79', null=False, blank=False, verbose_name='Номер телефона',
                           help_text='Введите номер с кодом страны')
    email = models.CharField(_('Email'), max_length=255, default=None, blank=True, null=True)
    # region = models.CharField(_('Страна'),max_length=20,default=GREATER,choices=GHANA_REGIONS,blank=False,null=True)

    education = models.CharField(_('Образование'), help_text='Уровень образования', max_length=38, default=SENIORHIGH,
                                 choices=EDUCATIONAL_LEVEL, blank=False, null=True)

    # COMPANY DATA
    department = models.ForeignKey(Department, verbose_name=_('Департамент'), on_delete=models.SET_NULL, null=True,
                                   default=None)
    role = models.ForeignKey(Role, verbose_name=_('Должность'), on_delete=models.SET_NULL, null=True, default=None)
    startdate = models.DateField(_('Дата приема на работу'), help_text='Дата по приказу', blank=False, null=True)
    employeetype = models.CharField(_('Тип сотрудника'), max_length=21, default=FULL_TIME, choices=EMPLOYEETYPE,
                                    blank=False, null=True)
    employeeid = models.CharField(_('Табельный номер сотрудника'), max_length=10, null=True, blank=True)
    dateissued = models.DateField(_('Дата выдачи пропуска'), help_text='Дата выдачи пропуска', blank=False, null=True)
    image = models.FileField(_('Изображение профиля'), upload_to='profiles', default='default.png', blank=True,
                             null=True,
                             help_text='Загрузи изображения не более 2.0 Мб')  # work on path username-date/image
    bio = models.CharField(_('Заметки'), help_text='Дополнительная информация', max_length=255, default='', null=True,
                           blank=True)
    is_terminated = models.BooleanField(default=False)

    # app related
    is_blocked = models.BooleanField(_('Is Blocked'), help_text='button to toggle employee block and unblock',
                                     default=False)
    is_deleted = models.BooleanField(_('Is Deleted'), help_text='button to toggle employee deleted and undelete',
                                     default=False)

    created = models.DateTimeField(verbose_name=_('Созданно'), auto_now_add=True, null=True)
    updated = models.DateTimeField(verbose_name=_('Обновлено'), auto_now=True, null=True)

    # PLUG MANAGERS
    objects = EmployeeManager()

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
        ordering = ['-created']

    def __str__(self):
        return self.get_full_name

    @property
    def get_full_name(self):
        fullname = ''
        firstname = self.firstname
        lastname = self.lastname
        othername = self.othername

        if (firstname and lastname) or othername is None:
            fullname = lastname + ' ' + firstname
            if othername:
                fullname = lastname + ' ' + firstname + ' ' + othername
            return fullname
        return

    @property
    def get_document_info(self):
        document_info = ''
        Document_series = self.Document_series
        Document_number = self.Document_number

        if Document_series and Document_number:
            document_info = Document_series + ' ' + Document_number

        return document_info

    @property
    def get_residence_address(self):
        address_parts = [attr for attr in
                         [self.Region, self.District, self.Settlement, self.Street, self.Home, self.Corps,
                          self.Apartment] if attr]

        return ', '.join(address_parts)

    @property
    def get_age(self):
        current_year = datetime.date.today().year
        dateofbirth_year = self.birthday.year
        if dateofbirth_year:
            return current_year - dateofbirth_year
        return

    @property
    def can_apply_leave(self):
        pass

    @property
    def get_pretty_birthday(self):
        if self.birthday:
            return self.birthday.strftime('%A,%d %B')  # Thursday,04 May -> staffs age privacy
        return

    @property
    def birthday_today(self):
        '''
        returns True, if birthday is today else False
        '''
        return self.birthday.day == datetime.date.today().day

    @property
    def days_check_date_fade(self):
        '''
        Check if Birthday has already been celebrated ie in the Past     ie. 4th May  & today 8th May 4 < 8 -> past else present or future '''
        return self.birthday.day < datetime.date.today().day  # Assumption made,If that day is less than today day,in the past

    def birthday_counter(self):
        '''
        This method counts days to birthday -> 2 day's or 1 day
        '''
        today = datetime.date.today()
        current_year = today.year

        birthday = self.birthday  # eg. 5th May 1995

        future_date_of_birth = datetime.date(current_year, birthday.month,
                                             birthday.day)  # assuming born THIS YEAR ie. 5th May 2019

        if birthday:
            if (future_date_of_birth - today).days > 1:

                return str((future_date_of_birth - today).days) + ' day\'s'

            else:

                return ' tomorrow'

        return

    def save(self, *args, **kwargs):

        '''
        overriding the save method - for every instance that calls the save method 
        perform this action on its employee_id
        added : March, 03 2019 - 11:08 PM

        '''

        get_id = self.employeeid  # grab employee_id number from submitted form field
        data = code_format(get_id)
        self.employeeid = data  # pass the new code to the employee_id as its original or actual code

        super().save(*args, **kwargs)  # call the parent save method
        # print(self.employeeid)


SICK = 'ежегодный основной оплачиваемый отпуск'
CASUAL = 'ежегодный дополнительный оплачиваемый отпуск'
EMERGENCY = 'отпуск без сохранения заработной платы'
STUDY = 'учебный отпуск'
BIRTH = 'отпуск по беременности и родам'
OTHER = 'другой'

LEAVE_TYPE = (
    (SICK, 'ежегодный основной оплачиваемый отпуск'),
    (CASUAL, 'ежегодный дополнительный оплачиваемый отпуск'),
    (EMERGENCY, 'отпуск без сохранения заработной платы'),
    (STUDY, 'учебный отпуск'),
    (BIRTH, 'отпуск по беременности и родам'),
    (OTHER, 'другой')
)

DAYS = 140


class Leave(models.Model):
    employee = models.ForeignKey('employee', on_delete=models.CASCADE, default=1, verbose_name='Сотрудник')
    startdate = models.DateField(verbose_name=_('Дата начала'), null=True, blank=False)
    enddate = models.DateField(verbose_name=_('Дата окончания'), null=True, blank=False)
    leavetype = models.CharField(choices=LEAVE_TYPE, max_length=44, default=SICK, null=True, blank=False,
                                 verbose_name='Тип отпуска')
    reason = models.CharField(max_length=255, help_text='Добавить дополнительную информацию для отпуска', null=True,
                              blank=True, verbose_name='Примечание')
    defaultdays = models.PositiveIntegerField(verbose_name=_('Количество дней отпуска в год счетчик'), default=DAYS,
                                              null=True, blank=True)

    # hrcomments = models.ForeignKey('CommentLeave') #hide

    status = models.CharField(max_length=12, default='pending')  # pending,approved,rejected,cancelled
    is_approved = models.BooleanField(default=False)  # hide

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = LeaveManager()

    class Meta:
        verbose_name = _('Leave')
        verbose_name_plural = _('Leaves')
        ordering = ['-created']  # recent objects

    def __str__(self):
        return '{0} - {1}'.format(self.leavetype, self.employee.user)

    @property
    def pretty_leave(self):
        leave = self.leavetype
        employee = self.employee.get_full_name
        return f'{employee} - {leave}'

    @property
    def leave_days(self):
        days_count = ''
        startdate = self.startdate
        enddate = self.enddate
        if startdate > enddate:
            return
        dates = (enddate - startdate)
        return dates.days

    @property
    def leave_approved(self):
        return self.is_approved == True

    @property
    def approve_leave(self):
        if not self.is_approved:
            self.is_approved = True
            self.status = 'approved'
            self.save()

    @property
    def unapprove_leave(self):
        if self.is_approved:
            self.is_approved = False
            self.status = 'pending'
            self.save()

    @property
    def leaves_cancel(self):
        if self.is_approved or not self.is_approved:
            self.is_approved = False
            self.status = 'cancelled'
            self.save()

    # def uncancel_leave(self):
    # 	if  self.is_approved or not self.is_approved:
    # 		self.is_approved = False
    # 		self.status = 'pending'
    # 		self.save()

    @property
    def reject_leave(self):
        if self.is_approved or not self.is_approved:
            self.is_approved = False
            self.status = 'rejected'
            self.save()

    @property
    def is_rejected(self):
        return self.status == 'rejected'


class Document(models.Model):
    employee = models.ForeignKey('employee', related_name='documents', on_delete=models.CASCADE,
                                 verbose_name='Сотрудник')
    document_file = models.FileField(_('Файл документа'), upload_to='documents/%Y/%m/%d/')
    filename = models.CharField(_('Название файла'), max_length=255)
    created = models.DateTimeField(verbose_name=_('Создано'), auto_now_add=True, null=True)
    updated = models.DateTimeField(verbose_name=_('Обновлено'), auto_now=True, null=True)

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование организации')
    leader_lastname = models.CharField(max_length=100, verbose_name='Фамилия руководителя')
    leader_name = models.CharField(max_length=100, verbose_name='Имя руководителя')
    leader_namemiddle = models.CharField(max_length=100, verbose_name='Отчество руководителя')
    position = models.CharField(max_length=100, verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class MilitaryRecord(models.Model):
    CATEGORIES = [
        ('военнообязанный', 'Военнообязанный'),
        ('запас', 'Запас'),
        ('не годный к службе', 'Не годный к службе'),
        ('подлежит призыву на ВС', 'Подлежит призыву на ВС'),
    ]
    RANKS = [
        ('рядовой', 'Рядовой'),
        ('ефрейтор', 'Ефрейтор'),
        ('младший сержант', 'Младший сержант'),
        ('сержант', 'Сержант'),
        ('старший сержант', 'Старший сержант'),

    ]
    CATEGORIES_RESERVE = [
        ('', ''),
        ('подлежит призыву на ВС', 'Подлежит призыву на ВС'),

    ]
    COMPOSITION = [
        ('офицеры', 'Офицеры'),
        ('прапорщики и мичманы', 'Прапорщики и мичманы'),
        ('сержанты и старшины', 'Сержанты и старшины'),
        ('солдаты и матросы', 'Солдаты и матросы'),

    ]

    employee = models.ForeignKey('employee', on_delete=models.CASCADE, verbose_name='Сотрудник')
    is_military_service = models.BooleanField(default=False, verbose_name='Военнообязанный')
    category = models.CharField(choices=CATEGORIES, max_length=50, verbose_name='Категория военного учета')
    military_ticket_number = models.CharField(max_length=50, verbose_name='Номер военного билета')
    issue_date = models.DateField(verbose_name='Дата выдачи')
    reserve_category = models.CharField(choices=CATEGORIES_RESERVE, max_length=50,
                                        verbose_name='Категория запаса')
    military_rank = models.CharField(choices=RANKS, max_length=50, verbose_name='Военное звание')
    composition = models.CharField(choices=COMPOSITION, max_length=50, verbose_name='Состав')
    code = models.CharField(max_length=150, verbose_name='Полное кодовое обозначение ВУС')
    vk_name = models.CharField(max_length=50, verbose_name='Наименование ВК')
    demobilization_mark = models.CharField(max_length=150, verbose_name='Отметка о снятии с ВУ')
    booking = models.BooleanField(default=False, verbose_name='Бронирование')
    mobilization_certificate = models.CharField(max_length=150, verbose_name='Мобилизационный талон')

    created = models.DateTimeField(verbose_name=_('Создано'), auto_now_add=True, null=True)
    updated = models.DateTimeField(verbose_name=_('Обновлено'), auto_now=True, null=True)


class Holiday(models.Model):
    date = models.DateField(_('Дата праздника'), unique=True)
    name = models.CharField(_('Название праздника'), max_length=100)
