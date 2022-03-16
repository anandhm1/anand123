from django import forms
from .models import Customer,LoanSaction

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class LoanSanctionForm(forms.ModelForm):
    class Meta:
        model = LoanSaction
        fields = '__all__'