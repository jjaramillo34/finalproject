from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(max_length=200)