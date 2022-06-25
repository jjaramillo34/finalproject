from django import forms
from contact.models import Contact

class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(max_length=200)