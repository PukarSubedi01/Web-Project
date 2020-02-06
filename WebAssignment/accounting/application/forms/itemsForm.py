from django import forms
from application.models.items import items




class itemForm(forms.ModelForm):
    class Meta:
        model=items
        fields="__all__"