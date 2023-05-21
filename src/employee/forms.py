from datetime import datetime

from django import forms
from employee.models import Role, Department, Nationality, Religion, Bank, Emergency, Relationship, Employee, Document, \
    Leave, Company
from django.contrib.auth.models import User


# EMPLoYEE
class EmployeeCreateForm(forms.ModelForm):
    employeeid = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Пожалуйста, введите цифры без пробелов'})
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={'onchange': 'previewImage(this);'})
    )
    birthday = forms.DateField(
        label='День рождения (YYYY-mm-dd)',
        widget=forms.DateInput(format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )
    Date_Registrations = forms.DateField(
        label='Дата регистрации (YYYY-mm-dd)',
        widget=forms.DateInput(format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )
    Date_issue = forms.DateField(
        label='Дата выдачи (YYYY-mm-dd)',
        widget=forms.DateInput(format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )
    startdate = forms.DateField(
        label='Дата приёма на работу (YYYY-mm-dd)',
        widget=forms.DateInput(format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )
    dateissued = forms.DateField(
        label='Дата выдачи пропуска (YYYY-mm-dd)',
        widget=forms.DateInput(format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Employee
        exclude = ['is_blocked', 'is_deleted', 'created', 'updated', 'is_terminated']
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 5, 'rows': 5})
        }

    # def clean_user(self):
    # 	user = self.cleaned_data['user'] #returns <User object>,not id as in [views <-> templates]

    # 	qry = Employee.objects.filter(user = user)#check, whether any employee exist with username - avoid duplicate users - > many employees
    # 	if qry:
    # 		raise forms.ValidationError('Employee exists with username already')
    # 	return user


class EmergencyCreateForm(forms.ModelForm):
    class Meta:
        model = Emergency
        fields = ['employee', 'fullname', 'tel', 'location', 'relationship']


# FAMILY

class FamilyCreateForm(forms.ModelForm):
    class Meta:
        model = Relationship
        fields = ['employee', 'status', 'spouse', 'occupation', 'tel', 'children', 'nextofkin', 'relationship']


class BankAccountCreation(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['employee', 'name', 'branch', 'account', 'salary']


class LeaveCreationForm(forms.ModelForm):
    reason = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        label='Причина'
    )

    class Meta:
        model = Leave
        exclude = ['defaultdays', 'hrcomments', 'status', 'is_approved', 'updated', 'created']
        fields = ['employee', 'leavetype', 'startdate', 'enddate', 'reason']


def clean_enddate(self):
    enddate = self.cleaned_data['Дата окончания']
    startdate = self.cleaned_data['Дата начала']
    today_date = datetime.date.today()

    if (startdate or enddate) < today_date:  # both dates must not be in the past
        raise forms.ValidationError("Выбранные даты неверны, пожалуйста, выберите еще раз")

    elif startdate >= enddate:  # TRUE -> FUTURE DATE > PAST DATE,FALSE other wise
        raise forms.ValidationError("Выбранные даты неверны")

    return enddate


class DocumentCreateForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['employee', 'document_file', 'filename']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['id', 'name', 'leader_lastname', 'leader_name', 'leader_namemiddle', 'position']
        widgets = {
        'name': forms.TextInput(attrs={'class': 'myformcontrol'}),
        'leader_lastname': forms.TextInput(attrs={'class': 'myformcontrol'}),
        'leader_name': forms.TextInput(attrs={'class': 'myformcontrol'}),
        'leader_namemiddle': forms.TextInput(attrs={'class': 'myformcontrol'}),
        'position': forms.TextInput(attrs={'class': 'myformcontrol'}),
        }


