from django import forms
from application.models.vendor import vendor
class vendorForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs= {
            'class': 'form-control',
            'placeholder': 'Full name',
            'size':'60'
            }
    )
    )
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'E-mail address',
            'size': '60',
            'type': 'email'
        }
    ))
    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '-- Enter phone number',
            'size': '60'
        }
    ))
    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '-- Enter address',
            'size': '60'
        }
    ))
    class Meta:
        model=vendor
        fields="__all__"

