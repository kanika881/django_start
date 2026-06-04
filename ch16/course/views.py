from django.shortcuts import render
def learn_django(req):
    return render("","course/django.html")
def learn_python(req):
    return render("","course/python.html")

# Create your views here.
