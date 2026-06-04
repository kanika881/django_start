from django.shortcuts import render

def home(req):
    return render("","core/home.html")
def about(req):
    return render("/about","core/about.html")
# Create your views here.
