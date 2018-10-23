from django import forms
from django.core.validators import RegexValidator

class ApplicationForm(forms.Form):
    First_Name = forms.CharField()
    Last_Name = forms.CharField()
    Email = forms.EmailField()
    phoneNumber = forms.CharField(
                required=True,
                validators=[
                    RegexValidator(
                        regex='^[0-9]+$',
                        message='Invalide phone number',
                    ),
                ])

class AdminLoginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
