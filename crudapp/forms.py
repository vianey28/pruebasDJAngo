from django import forms
from .models import Publisher

class FormularioPublisher(forms.ModelForm):
    class Meta:
        model = Publisher