from django.urls import path
from . import views

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

]
