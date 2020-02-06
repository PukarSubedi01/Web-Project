from django import forms
from application.models.customer import customer

class customerForm(forms.ModelForm):
    class Meta:
        model=customer
        fields="__all__"

