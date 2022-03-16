from django import forms
from .models import BaseInformatin,BankDetails,DocumentUpload

class BasicInformationForm(forms.ModelForm):
    class Meta:
        model = BaseInformatin
        fields = "__all__"

class BasicInforBankForm(forms.ModelForm):
    class Meta:
        model = BankDetails
        fields = "__all__"


class DocumentForm(forms.ModelForm):
    class Meta:
        model = DocumentUpload
        fields = "__all__"