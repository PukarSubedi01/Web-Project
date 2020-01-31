from django import forms
from application.models.bill import bill




class billForm(forms.ModelForm):
    class Meta:
        model=bill
        fields="__all__"