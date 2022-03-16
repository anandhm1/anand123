from django.urls import path
from . import views
urlpatterns = [
    path('show/',views.show,name = 'show'),
    path('accform/<int:id>',views.acc_headform, name = 'acc_form'),
    path('emi_details/<int:id>',views.emiview,name = 'emi'),
    path('acc_head_details/',views.account_head_data,name = 'loanee_data'),
    path('dummy/<int:id>',views.dummy,name = 'dummy'),
    path('loanee_customers/',views.loanee_customersview,name ='loan_cust_list'),

    #pdf URL
    #path('abc/', views.CustomerListView.as_view(), name='customer_list_view'),
    path('pdf/<int:id>/', views.emi_invoice_render_pdf_view, name='emi_invoice_pdf_view'),

    path('loan_details_email/',views.loan_details_email,name = 'loan_email'),
    path('email_response/',views.email_response_view,name = 'email_sent_response'),

    path('acc_dashboard/',views.dashboardview,name = 'acc_dashboard'),

    path('customer_response/<int:id>',views.customer_response_change_view,name = 'customer_response'),




]
