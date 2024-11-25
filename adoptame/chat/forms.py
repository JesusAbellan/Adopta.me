from django import forms
from .models import ChatMessage

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ('text',)
        labels = ({'text':'Mensaje'})
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control vw-75 rounded',
                'rows': 5
            })
        }
