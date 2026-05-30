from django.shortcuts import render
from django.http import HttpResponse

def learn_pandas(request,**kwargs):
    fees=kwargs.get("fees","200rs")
    return HttpResponse(f"learn pandas under {fees}")

# Create your views here.
