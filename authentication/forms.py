from django import forms
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username or Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class CustomRegistrationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password')