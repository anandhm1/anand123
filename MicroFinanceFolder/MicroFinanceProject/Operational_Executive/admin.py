from django.contrib import admin
from .models import CibilSc

class CustomeAdmin(admin.ModelAdmin):
    list_display = ['customer','cibil']
admin.site.register(CibilSc,CustomeAdmin)
