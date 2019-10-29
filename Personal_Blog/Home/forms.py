from django import forms
from django.forms import ModelForm

from .models import Subscriber

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password')


class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']