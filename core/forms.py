from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm): 
    username   = forms.CharField(widget=forms.TextInput())
    password   = forms.CharField(widget=forms.PasswordInput())
    

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username    = forms.CharField(widget=forms.TextInput())
    email       = forms.CharField(widget=forms.EmailInput())
    password1   = forms.CharField(widget=forms.PasswordInput())
    password2   = forms.CharField(widget=forms.PasswordInput())