from django import forms
from .models import formmodel

class regform(forms.ModelForm):
    class Meta:
        model=formmodel
        fields=["name","email","password"]
        widgets={
            "password":forms.PasswordInput
        }