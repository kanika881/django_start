from django.shortcuts import render
from lesson.form import Registration
def view_form(req):
    fm=Registration()
    return render(req,"lesson/form_view.html",{"form":fm})

# Create your views here.
