from django import forms
from lesson.models import reg_model
from django.core import validators
def validating_pwd_cpwd(value1,value2):
    if value1!=value2:
        raise forms.ValidationError("password not matching")
class reg_form(forms.ModelForm):
    class Meta:
        model=reg_model
        fields=["fname","lname","email","pwd","cpwd"]
        labels={
            "fname":"First Name",
            "lname":"Last Name",
            "email":"Email Id",
            "pwd":"Password",
            "cpwd":"Confirm Password"
            
        }
        error_messages={
            "email":{"required":"Email is required"},
            "fname":{"required":"First name is required"},
            "lname":{"required":"last name is required"},
            "pwd":{"required":"password is required"},
            "cpwd":{"required":"confirm password is required"}
            }
        widgets={
            "pwd":forms.PasswordInput(attrs={"class":"myclass"}),
            "cpwd":forms.PasswordInput(attrs={"class":"myclass"}),
            "fname":forms.TextInput(attrs={"class":"myclass","placeholder":"Enter First Nmae"}),
            "lname":forms.TextInput(attrs={"class":"myclass","placeholder":"Enter Last Nmae"})
            }
        validators={"cpwd":validating_pwd_cpwd(value1="cpwd",value2="pwd"),}