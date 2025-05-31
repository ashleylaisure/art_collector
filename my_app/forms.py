from django import forms
from .models import Copy

class CopyForm(forms.ModelForm):
    class Meta:
        model = Copy
        fields = ['artist', 'date', 'notes', 'image']
        widgets = {
            'date' : forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type' : 'date'
                }
            ),
        }