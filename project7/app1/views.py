from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_fun(request):
    return HttpResponse("hello from app1_fun")
def home(request):
    return HttpResponse("this is home page")
