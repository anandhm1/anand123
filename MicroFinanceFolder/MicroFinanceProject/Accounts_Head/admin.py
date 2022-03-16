from django.contrib import admin
from .models import Account_Head
class Account_Head_Admin(admin.ModelAdmin):
    list_display = ['loan_id','sanction_amt','rate_of_interest','loan_tenure','total_amt','is_customer_responsed']
admin.site.register(Account_Head,Account_Head_Admin)