from django.shortcuts import render
def learn_python(req):
    course_details={"course_name":"ruby","version":"3.1.9","duration":"3 months"}
    return render(req,"course1/python.html",context=course_details)


# Create your views here.
