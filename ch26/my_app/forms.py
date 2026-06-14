from django import forms
from django.core import validators

class my_form(forms.Form):
    error_css_class="myerror"
    requiered_css_class="required"
    first_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"enter first name"}),validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(3)],error_messages={"required":"invalid first name"})
    last_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"enter last name"}),validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(3)])
    pwd=forms.CharField(widget=forms.PasswordInput(),)
    email=forms.EmailField(widget=forms.EmailInput())
    