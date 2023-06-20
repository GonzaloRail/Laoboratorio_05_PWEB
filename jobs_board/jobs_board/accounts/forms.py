from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')