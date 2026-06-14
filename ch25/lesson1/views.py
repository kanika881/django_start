from django.shortcuts import render
from django.http import HttpResponseRedirect
from lesson1.forms import reg_form
def reg_view(req):
    
    if req.method=="POST":
        fm=reg_form(req.POST)
        if fm.is_valid():
            fullname=fm.cleaned_data["fname"]
            email_id=fm.cleaned_data["email"]
            father_name=fm.cleaned_data["father_name"]
            print("name:",fullname)
            print("father name:",father_name)
            print("email id:",email_id)
        # if fm.is_valid():
        #     print("VALID")
            return HttpResponseRedirect("/st/register")
        # else:
        #     print("ERRORS:", fm.errors)
            
            
    else:
        fm=reg_form()
    return render(req,"lesson1/reg.html",{"form":fm})

# Create your views here.
