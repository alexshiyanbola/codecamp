from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

from userprofile.models import Customer
#    For default  user signup 
class SignupForm(UserCreationForm):
    username = forms.CharField( max_length=50, required=True)
    first_name = forms.CharField( max_length=50, required=True)
    last_name = forms.CharField( max_length=50, required=True)
    email = forms.EmailField( required=True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

# for profile
class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ['username','first_name','last_name','phone','email','address','pix']
