from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
                                'placeholder': 'Tu nombre de usuario',
                                'class': 'col-12 rounded-3 border-0',
                                'style': 'height:3em'
                                }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
                                'placeholder': 'Tu dirección de correo',
                                'class': 'col-12 rounded-3 border-0',
                                'style': 'height:3em'
                                }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
                                'placeholder': 'Tu contraseña',
                                'class': 'col-12 rounded-3 border-0',
                                'style': 'height:3em'
                                }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                                'placeholder': 'Repite tu contraseña',
                                'class': 'col-12 rounded-3 border-0',
                                'style': 'height:3em'
                                }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
                                'placeholder': 'Tu nombre de usuario',
                                'class': 'col-12 rounded-3 border-0',
                                'style': 'height:3em'
                                }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                                'placeholder': 'Tu contraseña',
                                'class': 'col-12 rounded-3 border-0',
                                'style': 'height:3em'
                                }))
