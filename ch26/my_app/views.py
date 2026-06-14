from django.shortcuts import render
from my_app.forms import my_form
from django.http import HttpResponseRedirect
from my_app.models import form_data

def my_form_view(req):
    if req.method=="POST":
        fm=my_form(req.POST)
        if fm.is_valid():
            fname=fm.cleaned_data["first_name"]
            lname=fm.cleaned_data["last_name"]
            pwd=fm.cleaned_data["pwd"]
            email=fm.cleaned_data["email"]
            user=form_data(fname=fname,lname=lname,pwd=pwd,email=email)
            user.save()
            return HttpResponseRedirect("/all/form")
    else:
        fm=my_form()
    return render(req,"my_app/my_app_form.html",{"form":fm})

# Create your views here.
