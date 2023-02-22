from .models import User
from django import forms
from django.core import validators
class EmpReg(forms.ModelForm):
    
    class Meta:
        model=User
        fields=['emname','ememail','designation','photo']
        
