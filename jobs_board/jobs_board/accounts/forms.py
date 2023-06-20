from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'input-field'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'input-field'}))

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'input-field'}))
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'input-field'}))
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'class': 'input-field'}))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')