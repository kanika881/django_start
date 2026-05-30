from django.shortcuts import render
def learn_django(req):
    version="6.X"
    return render(req,"core/django.html",{"vers":version})
# Create your views here.
