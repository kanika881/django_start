from django.shortcuts import render
from student.models import register_d,Login

def stu_info(req):
    stu_data=register_d.objects.all()
    log_data=Login.objects.all()
    return render(req,"student/stu_info.html",{"data":stu_data,"log_data":log_data})

# Create your views here.
