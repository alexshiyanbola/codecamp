from dataclasses import fields
from pyexpat import model
from turtle import mode
from django import forms
from . models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name','last_name','email','message']
        
        
       