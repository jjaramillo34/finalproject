from django import forms
from django.urls import reverse_lazy
from comment.models import Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widget = {
            'name': forms.TextInput(attrs={'class' : 'form-group'}),
            'email': forms.TextInput(attrs={'class' : 'form-group'}),
            'body': forms.Textarea(attrs={'class' : 'form-group'}),
        }
        
    

#class CommentForm(forms.Form):
#    #model = Comment
#    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
#    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
#    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your text'}))
#        fields = ['name', 'email', 'body']
#class CrispyCommentForm(CommentForm):
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.helper = FormHelper()
#        self.helper.layout = Layout(
#            Row(
#                Column('name', css_class='form-group col-md-6 mb-0'),
#                Column('email', css_class='form-group col-md-6 mb-0'),
#                Column('body', css_class='form-group col-md-6 mb-0'),
#                css_class='form-row'
#            ),
#            Submit('submit', 'Sign in')
#        )