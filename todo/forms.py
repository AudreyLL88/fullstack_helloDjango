from django import forms
from .models import Items


class ItemForms(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'done']
