from django import forms
from application.models.user import user

class userForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs= {
            'class': 'form-control',
            'placeholder': 'Enter your name',
            'size':'60',
            'id' : 'fullname'
            }
    )
    )
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'E-mail address',
            'size': '60',
            'type': 'email',
            'id': 'email'
        }
    ))
    password = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Re-type password',
            'size': '60',
            'type': 'password',
            'id': 're-password'
        }
    ))

    class Meta:
        model=user
        fields="__all__"
