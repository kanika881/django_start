from django import forms
class log_form(forms.Form):
    name=forms.CharField(label="FullName",max_length=100,label_suffix=":",initial="Enter ur full name",help_text="enter ur legal name",validators=["MinLengthValidator(3)"])
    email=forms.EmailField(label="Email Address",label_suffix=":",disabled=False)
    pincode=forms.IntegerField(label="PinCode",label_suffix=":",min_value=100000,max_value=999999,error_messages={
        "min_vallue":"pincode must be greater than this value",
        "max_vallue":"pincode must be lesser than this value"})
    age=forms.FloatField(label="Age",label_suffix=":",min_value=0)
    date_birth=forms.DateField(label="DOB",required=False,help_text="please enter in 'DD-MM-YYYY'")
    aptime=forms.TimeField(label="Appointemnt Time",label_suffix=":",required=False)
    is_subscribed=forms.BooleanField(label="Subscribe To News Letter",label_suffix=":",required=False)
    agree_terms=forms.NullBooleanField(label="Do u Agree with terms")
    gender=forms.ChoiceField(label="Gender",label_suffix=":",choices=[('M','Male'),('F','Female'),('O',"Other")])
    interest=forms.MultipleChoiceField(label="Interest",choices=[("pcm","intelligent"),("bio","Doctor"),("arts","lawyer")])
    profile_image=forms.ImageField(label="Profile photo",required=True)
    resume=forms.FileField(label="Resume",required=True)
    Github=forms.URLField(label="Github Link",required=True)
    Phone=forms.RegexField(label="Phone No:",regex=r'^\+?1?\d{9,15$}',error_messages={"invalid":"Enter a valid phone no"})
    pwd=forms.CharField(label="password",max_length=50,widget=forms.PasswordInput(),validators=["MinlengthValdator(8)"])
    ip=forms.GenericIPAddressField(label="IP Address",protocol="both",unpack_ipv4=False,localize=True)
    rate=forms.DecimalField(label="Rate",decimal_places=2,min_value=0,max_value=10,max_digits=3,initial=0.0,localize=True)
    
class reg_form(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"john","label":"FullName"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"required":False,"label":"Email Address"}))
    pincode=forms.IntegerField(label="PinCode",label_suffix=":",min_value=100000,max_value=999999,error_messages={
        "min_vallue":"pincode must be greater than this value",
        "max_vallue":"pincode must be lesser than this value"})
    age=forms.FloatField(label="Age",label_suffix=":",min_value=0)
    