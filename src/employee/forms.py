from django import forms
from employee.models import Role, Department, Nationality, Religion, Bank, Emergency, Relationship, Employee
from django.contrib.auth.models import User


# EMPLoYEE
class EmployeeCreateForm(forms.ModelForm):
    employeeid = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Пожалуйста, введите 5 символов без символов и косых черт, например, A0025'})
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
        exclude = ['is_blocked', 'is_deleted', 'created', 'updated']
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
