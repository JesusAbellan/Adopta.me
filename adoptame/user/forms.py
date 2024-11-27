from django import forms
from .models import PetOwner


class EditPetOwnerForm(forms.ModelForm):
    class Meta:
        model = PetOwner
        fields = ('username', 'email', 'is_shelter')
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
    is_shelter = forms.BooleanField(widget=forms.CheckboxInput(attrs={
                                    'class': 'form-check-input'
                                    }))