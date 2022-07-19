from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Contact

class ContactForm(forms.ModelForm):
    email = forms.EmailField(label=_(u'E-Mail:'))
    subject = forms.CharField(max_length=100, label=_(u'Subject:'))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':6}), label=_(u'Message:'))
    class Meta:
        model = Contact
        fields = ['email', 'subject', 'message']
        
    def clean_email(self):
        email = self.cleaned_data['email']
        domain = email.split('@')[1]
        if domain != 'gmail.com':
            raise forms.ValidationError((u"The domain %s could not be found."))
        return email
    
    def clean_subject(self):
        subject = self.cleaned_data['subject']
        if len(subject) < 10:
            raise ValidationError("Subject must be at least 10 characters!")
        elif len(subject) == 0:
            raise ValidationError("Subject cannot be empty!")
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return subject

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 10:
            raise ValidationError("Message must be at least 10 characters!")
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return message

#class ContactForm(forms.Form):
#    email = forms.EmailField(
#        label="email",
#        max_length=30,
#        required=True,
#        widget=forms.TextInput(),
#        help_text="Insert your email",
#    )
#    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
#    message = forms.CharField(
#        label='Message',
#        widget=forms.Textarea()
#    )
    