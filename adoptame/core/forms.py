from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import PetOwner as User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    FORMCLASS ='col-12 rounded-3'

    username = forms.CharField(widget=forms.TextInput(attrs={
                                'placeholder': 'Tu nombre de usuario',
                                'class': FORMCLASS,
                                'style': 'height:3em'
                                }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
                                'placeholder': 'Tu dirección de correo',
                                'class': FORMCLASS,
                                'style': 'height:3em'
                                }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
                                'placeholder': 'Tu contraseña',
                                'class': FORMCLASS,
                                'style': 'height:3em'
                                }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                                'placeholder': 'Repite tu contraseña',
                                'class': FORMCLASS,
                                'style': 'height:3em'
                                }))


class LoginForm(AuthenticationForm):
    FORMCLASS ='col-12 rounded-3'

    username = forms.CharField(widget=forms.TextInput(attrs={
                                'placeholder': 'Tu nombre de usuario',
                                'class': FORMCLASS,
                                'style': 'height:3em'
                                }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                                'placeholder': 'Tu contraseña',
                                'class': FORMCLASS,
                                'style': 'height:3em'
                                }))
