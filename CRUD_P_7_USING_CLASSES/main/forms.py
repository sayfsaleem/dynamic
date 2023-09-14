from django.forms import ModelForm
from .models import UserRegistration
from django.core import validators
from django import forms
class UsersReg(ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['name','email','passcode',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'passcode': forms.PasswordInput(attrs={'class': 'form-control'},render_value=True),
        }