from django import forms
from application.models.vendor import vendor
class vendorForm(forms.ModelForm):
    class Meta:
        model=vendor
        fields="__all__"

