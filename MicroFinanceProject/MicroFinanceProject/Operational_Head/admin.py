from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_id','first_name','last_name','personal_details','occupational_details','cibil']
admin.site.register(Customer,CustomerAdmin)
