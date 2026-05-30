from django.shortcuts import render
from django.http import HttpResponse

def app1_fun(request,**kwargs):
    status=kwargs.get("status","noee")
    return HttpResponse(f"<h1>hi this is me app1 {status}</h1>")


# Create your views here.
