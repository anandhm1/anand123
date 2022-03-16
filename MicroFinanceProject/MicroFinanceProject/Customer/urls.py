from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('Mainhomepage/',Mainhomepage,name='Mainhomepage'),
    path('LoanEnquiry/',LoanEnquiry,name='LoanEnquiry'),
    path('ApplicationStatus/',ApplicationTable,name='ApplicationStatus'),
    path('EMICalculator/',EMICalculator,name='EMICalculator'),
    path('ApprovedLoan/', ApprovedLoanView, name='ApprovedLoan'),
    path('AgrementView/', AgrementView, name='agrement'),
    path('show/',show1, name='show1'),


  path('change-password/',auth_views.PasswordChangeView.as_view(template_name='Customer/PasswordTemplates/changepassword.html'),name='change-password'),
  path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name="Customer/PasswordTemplates/password_change_done.html"),name='password_change_done'),
  path('reset_password/', auth_views.PasswordResetView.as_view(template_name="Customer/PasswordTemplates/reset_password.html"),name='reset_password'),
  path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="Customer/PasswordTemplates/password_reset_sent.html"),name='password_reset_done'),
  path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="Customer/PasswordTemplates/password_reset_form.html"),name='password_reset_confirm'),
  path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="Customer/PasswordTemplates/password_reset_done.html"),name='password_reset_complete')
]