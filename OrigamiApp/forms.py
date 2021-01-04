from django import forms
from django.contrib.auth.models import User
from OrigamiApp.models import UserProfile

class UserSignUp(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class UserProfileSignUp(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ['pic']