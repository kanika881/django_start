from django.shortcuts import render
from django.http import HttpResponse

def myfunction(request):
    return HttpResponse("hello its me")

# Create your views here.
