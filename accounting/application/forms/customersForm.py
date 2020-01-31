from django import forms
from application.models.customer import customer

class customerForm(forms.ModelForm):
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
            'placeholder': '-- Enter Phone Number',
            'size': '60'
        }
    ))
    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '-- Enter Address',
            'size': '60'
        }
    ))
    class Meta:
        model=customer
        fields="__all__"

