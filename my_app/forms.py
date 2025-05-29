from django import forms
from .models import Copy

class CopyForm(forms.ModelForm):
    class Meta:
        model = Copy
        fields = '__all__'