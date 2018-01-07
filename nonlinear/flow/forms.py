from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='subject', max_length=255)
    message = forms.CharField(label='message', widget=forms.Textarea)
    email = forms.CharField(label='email', max_length=255)