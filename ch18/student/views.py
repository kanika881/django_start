from django.shortcuts import render
from student.models import profile
def all(req):
    stu=profile.objects.all()
    # print(stu)
    return render(req,"student/all_data.html",{"students":stu})
def single(req):
    stu=profile.objects.get(id=1)
    # print(stu)
    return render(req,"student/single_data.html",{"student":stu})

# Create your views here.
