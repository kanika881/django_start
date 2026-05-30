from django.shortcuts import render
from django.http import HttpResponse

def app2_fun(request):
    return HttpResponse("this is app2 fun")

# Create your views here.
