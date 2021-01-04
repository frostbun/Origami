from django import forms
from django.contrib.auth.models import User
from OrigamiApp.models import UserProfile

class UserSignUp(forms.ModelForm):
    password = forms.CharField(widget = [forms.PasswordInput(), ])

    class Meta():
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']