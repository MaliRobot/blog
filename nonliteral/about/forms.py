from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class ContactForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    subject = forms.CharField(label='subject', max_length=255, widget=forms.TextInput(
        attrs={
            'placeholder': 'subject',
            'required': True
        }))
    message = forms.CharField(label='message', widget=forms.Textarea(
        attrs={
            'placeholder': 'message',
            'required': True
        }))
    email = forms.EmailField(label='email', max_length=255, widget=forms.EmailInput(
        attrs={
            'placeholder': 'email',
            'required': True
        }))
