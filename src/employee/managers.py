from django.db import models
import datetime


class EmployeeManager(models.Manager):
    def get_queryset(self):
        '''
        Employee.objects.all() -> returns only active employees ie.is_deleted = False
        '''
        return super().get_queryset().filter(is_deleted=False)

    def all_employees(self):
        '''
        Employee.objects.all_employee() -> returns all employees including deleted one's
        NB: don't specify filter. ***
        '''
        return super().get_queryset()

    def all_blocked_employees(self):
        '''
        Employee.objects.all_blocked_employees() -> returns list of blocked employees ie.is_blocked = True
        '''
        return super().get_queryset().filter(is_blocked=True)

    def birthdays_current_month(self):
        '''
        This Method Fetches all the active users,whose date of birthday is in current month, "this month".
        Every month list all employees whose birthday is in that month.

        HowTo: Employee.objects.birthdays_current_month()

        '''
        current_date = datetime.date.today()
        return super().get_queryset().filter(is_blocked=False).filter(birthday__month=current_date.month)


class LeaveManager(models.Manager):
    def get_queryset(self):
        '''
		overrides objects.all()
		return all leaves including pending or approved
		'''
        return super().get_queryset()

    def all_pending_leaves(self):
        '''
		gets all pending leaves -> Leave.objects.all_pending_leaves()
		'''
        return super().get_queryset().filter(status='pending').order_by('-created')  # applying FIFO

    def all_cancel_leaves(self):
        return super().get_queryset().filter(status='cancelled').order_by('-created')

    def all_rejected_leaves(self):
        return super().get_queryset().filter(status='rejected').order_by('-created')

    def all_approved_leaves(self):
        '''
		gets all approved leaves -> Leave.objects.all_approved_leaves()
		'''
        return super().get_queryset().filter(status='approved')

    def current_year_leaves(self):
        '''
		returns all leaves in current year; Leave.objects.all_leaves_current_year()
		or add all_leaves_current_year().count() -> int total
		this include leave approved,pending,rejected,cancelled

		'''
        return super().get_queryset().filter(startdate__year=datetime.date.today().year)
