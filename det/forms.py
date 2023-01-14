from .models import User
from django import forms
from django.core import validators
class EmpReg(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        # labels={'name':'Enter name'}
        # error_messages={'name':{'required':'name ta lekhnai parxa'}}
       

