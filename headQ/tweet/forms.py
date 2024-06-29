from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
'''
class UserRegistrationForm(UserCreationForm):
    '''