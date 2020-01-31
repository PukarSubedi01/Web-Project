from django import forms
from application.models.invoice import invoice




class invoiceForm(forms.ModelForm):
    class Meta:
        model=invoice
        fields="__all__"