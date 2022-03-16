from django import forms
from .models import Account_Head,Emi_Model

class Account_Head_Form(forms.ModelForm):
    sanction_amt = forms.FloatField()

    class Meta:
        model = Account_Head
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #
    #     initial = kwargs.pop('initial', {})
    #     self.person = kwargs.pop('sanction_amt')
    #     for key in self.initial_fields:
    #         if hasattr(self.sanction_amt, key):
    #             initial[key] = initial.get(key) or getattr(self.sanction_amt, key)
    #     kwargs['initial'] = initial
    #     super(Account_Head_Form, self).__init__(*args, **kwargs)


class Emi_Model_Form(forms.ModelForm):
    class Meta:
        model = Emi_Model
        fields = '__all__'
