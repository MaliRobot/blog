# story/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ReaderUser


class ReaderUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = ReaderUser
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].widget.attrs['class'] = 'form-control'


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
