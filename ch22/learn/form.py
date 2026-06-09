from django import forms

class reg(forms.Form):
    fname=forms.CharField(initial="",help_text="write full name")
    phone_no=forms.IntegerField()
    age=forms.IntegerField()
    Date_Of_Birth=forms.DateField()
class log(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    Date_Of_Birth=forms.DateField()
    Meeting_Time=forms.TimeField()
    key=forms.CharField(widget=forms.HiddenInput())
    Slug=forms.SlugField()
    
    