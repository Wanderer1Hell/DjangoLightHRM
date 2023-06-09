from django.urls import path
from . import views
from .views import sick_leave

app_name = 'dashboard'

urlpatterns = [
    path('welcome/', views.dashboard, name='dashboard'),

    # Employee
    path('employees/all/', views.dashboard_employees, name='employees'),
    path('employee/create/', views.dashboard_employees_create, name='employeecreate'),
    path('employee/profile/<int:id>/', views.dashboard_employee_info, name='employeeinfo'),
    path('employee/profile/edit/<int:id>/', views.employee_edit_data, name='edit'),
    path('employees/<int:employee_id>/delete/', views.dashboard_employee_delete, name='employeedelete'),
    path('employee/terminate/<int:id>/', views.employee_terminate, name='employee_terminate'),
    path('employees/restore/<int:id>/', views.employee_unterminate, name='employee_unterminate'),

    # Emergency
    path('emergency/create/', views.dashboard_emergency_create, name='emergencycreate'),
    path('emergency/update/<int:id>', views.dashboard_emergency_update, name='emergencyupdate'),

    # Family
    path('family/create/', views.dashboard_family_create, name='familycreate'),
    path('family/edit/<int:id>', views.dashboard_family_edit, name='familyedit'),

    # Bank
    path('bank/create/', views.dashboard_bank_create, name='bankaccountcreate'),
    path('bank/edit/<int:id>/', views.employee_bank_account_update, name='accountedit'),
    # Document
    path('document/create/', views.dashboard_document_create, name='documentcreate'),
    path('document/delete/<int:id>/', views.dashboard_document_delete, name='documentdelete'),
    path('document/update/<int:id>', views.dashboard_document_edit, name='documentedit'),
    path('document/generate', views.fill_template, name='filltemplate'),
    path('document/generate-t8', views.fill_template_t8, name='filltemplate_t8'),
    path('document/generate-t6', views.fill_template_t6, name='filltemplate_t6'),
    path('document/generate-t11', views.fill_template_t11, name='filltemplate_t11'),
    path('document/generate-t2', views.fill_template_t2, name='filltemplate_t2'),
    # Military
    path('military/create/', views.dashboard_military_create, name='militarycreate'),
    path('military/update/<int:id>', views.dashboard_military_update, name='militaryupdate'),

    # Shedules
    path('employee_info_schedule/', views.employee_info_schedule, name='employee_info_schedule'),
    path('work_schedule/<int:employee_id>/', views.work_schedule, name='work_schedule'),

    # ---work-on-edit-view------#
    path('leave/apply/', views.leave_creation, name='createleave'),
    path('leaves/pending/all/', views.leaves_list, name='leaveslist'),
    path('leaves/approved/all/', views.leaves_approved_list, name='approvedleaveslist'),
    path('leaves/cancel/all/', views.cancel_leaves_list, name='canceleaveslist'),
    path('leaves/all/view/<int:id>/', views.leaves_view, name='userleaveview'),
    path('leaves/view/table/', views.view_my_leave_table, name='staffleavetable'),
    path('leave/approve/<int:id>/', views.approve_leave, name='userleaveapprove'),
    path('leave/unapprove/<int:id>/', views.unapprove_leave, name='userleaveunapprove'),
    path('leave/cancel/<int:id>/', views.cancel_leave, name='userleavecancel'),
    path('leave/uncancel/<int:id>/', views.uncancel_leave, name='userleaveuncancel'),
    path('leaves/rejected/all/', views.leave_rejected_list, name='leavesrejected'),
    path('leave/reject/<int:id>/', views.reject_leave, name='reject'),
    path('leave/unreject/<int:id>/', views.unreject_leave, name='unreject'),

    # BIRTHDAY ROUTE
    path('birthdays/all/', views.birthday_this_month, name='birthdays'),

    # Organizational data
    path('company/all/', views.company_list, name='companylist'),
    path('company/update/<int:id>/', views.company_create_or_update, name='companyupdate'),
    path('company/delete/<int:id>/', views.company_delete, name='companydelete'),

    # Holiday
    path('holidays/', views.holiday_request, name='holiday_request'),
    path('holiday-delete/<int:holiday_id>/', views.holiday_delete, name='holiday_delete'),

    # Experience
    path('employment_history/add/<int:employee_id>/', views.employment_history_add, name='employment_history_add'),
    path('employment_history/edit/<int:employment_history_id>/', views.employment_history_edit,
         name='employment_history_edit'),

    # Sick days
    path('sick-leave/', sick_leave, name='sick_leave'),
    path('sick-leave/delete/<int:sick_leave_id>/', views.delete_sick_leave, name='delete_sick_leave'),

]
