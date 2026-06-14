from django.shortcuts import render
from django.contrib import messages
from .forms import regform

from django.http import HttpResponseRedirect
def home(req):
    # messages.add_message(req,messages.SUCCESS,"your account has been created!!")
    # messages.add_message(req,messages.INFO,"this is info!!!!")
    # messages.add_message(req,messages.WARNING,"this is warn!!!")
    messages.success(req,"this is success")
    messages.warning(req,"this is warning")
    messages.info(req,"this is info")
    messages.error(req,"this is danger")
    messages.debug(req,"this is debug")
    print(messages.get_level(req))
    messages.set_level(req,messages.DEBUG)
    messages.debug(req,"this is debug after setup")
    return render(req,"lesson/home.html")

def register(req):
    if req.method=="POST":
        fm=regform(req.POST)
        if fm.is_valid:
            fm.save()
            messages.success(req,"This is Success!!!")
            return HttpResponseRedirect("/register/")
            
    else:   
        fm=regform()
    return render(req,"lesson/register.html",{"form":fm})
