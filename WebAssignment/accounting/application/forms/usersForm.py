from django import forms
from application.models.user import user

class userForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(
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
    password = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Create password',
            'size': '60',
            'type': 'password'
        }
    ))
    class Meta:
        model=user
        fields="__all__"
