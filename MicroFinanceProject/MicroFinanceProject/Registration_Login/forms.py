from django import forms
from django.contrib.auth.forms import User, UserCreationForm
import re

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email']


    def clean_email(self):
        email=self.cleaned_data.get('email')
        domain=['gmail.com','yahoo.com','hotmail.com']

        slpit_list=email.split('@')

        if slpit_list[1] not in domain:
            raise forms.ValidationError("Please Enter Correct domain name")
        return email

    def clean_pancard_no(self):
        pancard_no=self.cleaned_data.get("pancard_no")

        result=re.compile("[A-Z]{5}\[0-9]{4}\[A-Z]{1}")

        if result.match(pancard_no) == False:
            raise forms.ValidationError("Invalid PanCard Number")
        return pancard_no