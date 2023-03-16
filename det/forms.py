from .models import Employee
from django import forms
from django.core import validators
class EmpReg(forms.ModelForm):
    
    class Meta:
        model=Employee
        fields=['emname','ememail','salary','designation',]
        
