from django.shortcuts import render
from registration.form import log_form
def log_view(req):
    fm=log_form()
    return render(req,"registration/log.html",{"form":fm})
# Create your views here.
