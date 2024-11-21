from django import forms
from .models import Pet, Race

INPUT_CLASSES = 'w-75 py-2 px-3 rounded border bg-white'
FORM_CONTROL = INPUT_CLASSES + ' form-control'
FORM_SELECT = INPUT_CLASSES + ' form-select selectpicker'

class NewPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('specie', 'race', 'name', 'description', 'image', 'age')

        widgets = {
            'specie': forms.Select(attrs={
                'class': FORM_SELECT,
            }),
            'race': forms.Select(attrs={
                'class': FORM_SELECT,
                'data-live-search': 'true',
            }),
            'name': forms.TextInput(attrs={
                'class': FORM_CONTROL,
            }),
            'description': forms.Textarea(attrs={
                'class': FORM_CONTROL,
            }),
            'age': forms.NumberInput(attrs={
                'class': FORM_CONTROL,
            }),
            'image': forms.FileInput(attrs={
                'class': FORM_CONTROL,
            }),
        }

class EditPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('race', 'name', 'description', 'image', 'age', 'is_adopted')

        widgets = {
            'race': forms.Select(attrs={
                'class': FORM_SELECT,
                'data-live-search': 'true',
            }),
            'name': forms.TextInput(attrs={
                'class': FORM_CONTROL,
            }),
            'description': forms.Textarea(attrs={
                'class': FORM_CONTROL,
            }),
            'age': forms.NumberInput(attrs={
                'class': FORM_CONTROL,
            }),
            'image': forms.FileInput(attrs={
                'class': FORM_CONTROL,
            }),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['race'].queryset = Race.objects.none()
