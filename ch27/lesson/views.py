from django.shortcuts import render
from lesson.forms import reg_form
from lesson.models import reg_model
from django.http import HttpResponseRedirect
def reg_view(req):
    if req.method=="POST":
        form=reg_form(req.POST)
        if form.is_valid():
            nm=form.cleaned_data["fname"]
            lnm=form.cleaned_data["lname"]
            email=form.cleaned_data["email"]
            pwd=form.cleaned_data["pwd"]
            cpwd=form.cleaned_data["cpwd"]
            user=reg_model(fname=nm,lname=lnm,email=email,pwd=pwd)
            user.save()
            return HttpResponseRedirect("/st/lesson")
    else:
        form=reg_form()
    return render(req,"lesson/reg.html",{"form":form})
        

# Create your views here.
