from django import forms
from django.core import validators

def start_with_s(value):
    if value[0]!="s":
        raise forms.ValidationError("email should start with s ")
class reg_form(forms.Form):
    fname=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Type Here"}),label="Full Name")
    father_name=forms.CharField(validators=[validators.MaxLengthValidator(8)])
    pwd=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"please enter strong password"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"please enter valid email"}) , validators=[start_with_s])
    About=forms.CharField(widget=forms.Textarea(attrs={"placeholder":"please enter about yourself"}))
    is_viewer=forms.BooleanField(widget=forms.CheckboxInput())
    
    # using django validation for specific fields
    
    
    # def clean_fname(self):
    #     name=self.cleaned_data["fname"]
    #     if len(name)<4:
    #         raise forms.ValidationError("enter more than or equal to 4 char")
    #     return name
    # def clean_email(self):
    #     email=self.cleaned_data["email"]
    #     if len(email)<10:
    #         raise forms.ValidationError("please enter a valid email")
    #     return email
    
    
    # django validation all at once 
    
    def clean(self):
        cleaned_data=super().clean()
        fname_value=cleaned_data.get("fname")
        email_value=cleaned_data.get("email")
        if fname_value and len(fname_value)<4:
            self.add_error("fname","enter more than or equal to 4 char")
        if email_value and len(email_value)<10:
            self.add_error("email","please enter a valid email")
        return cleaned_data
            