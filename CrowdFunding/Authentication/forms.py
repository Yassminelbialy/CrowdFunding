from django import forms
from django.contrib.auth.models import User
from Authentication.models import Users
from django.db import models
from django.forms import ModelForm

# from .validators import validate_even

class UserForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password', 'is_active')
