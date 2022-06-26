from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widget = {
            'email': forms.TextInput(attrs={'class' : 'form-group'}),
            'subject': forms.TextInput(attrs={'class' : 'form-group'}),
            'message': forms.Textarea(attrs={'class' : 'form-group'}),
        }