from django.shortcuts import render
from datetime import datetime
# # exmaple 1.1
# def learn_django(req):
#     course="python"
#     return render(req,'course/django.html',{"course":course})
# exmaple 1.2
# def learn_django(req):
#     course_details={"cname":"python",
#                     "duration":"5 mnths",
#                     "fees":3000}
#     return render(req,'course/django.html',{"course":course_details})
# example 2.1
# def learn_django(req):
#     course_details={"cname":"python",
#                     "duration":"5 mnths",
#                     "fees":3000}
#     return render(req,'course/django.html',{"course":course_details})
# example 2.2
# def learn_django(req):
#     course="Django"
#     return render(req,'course/django.html',context={"course":course})
# example 3 
# def learn_django(req):
#     dt=datetime.now()
    
#     return render(req,'course/django.html',context={"time":dt})
# example 4 : float tag
# def learn_django(req):
#     nums={
#         "num1":12.78965,
#         "num2":3.5000,
#         "num3":87.23
        
#     }
#     return render(req,'course/django.html',context={"float_nums":nums})
# example 5.1-> If tag
# def learn_django(req):
#     course="django"
#     return render(req,'course/django.html',context={"cname":course})
# # example 5.2-> If tag
# def learn_django(req):
#     course="True"
#     return render(req,'course/django.html',context={"cname":course})
# example 5.3-> If tag
# def learn_django(req):
#     course="True"
#     num=3
#     return render(req,'course/django.html',context={"cname":course,"numb":num})
# example 5.4 if else tag
# def learn_django(req):
#     course="django"
#     num=3
#     return render(req,'course/django.html',context={"cname":course,"numb":num})

# example 6 for tag 
# def learn_django(req):
#     student={"names":["kanika","arman","ajay","ajay"]}
#     return render(req,'course/django.html',context=student)
# example 7 
# def learn_django(req):
#     students={"stud1":{"name":"rashii","age":32},
#              "stud2":{"name":"komal","age":12},
#              "stud3":{"name":"raj","age":19}
#     }
    
#     return render(req,'course/django.html',context={"stud":students})
# example 8 
def learn_django(req):
    student={
        "name":"raman",
        "gender":"male",
        "age":23
    }
    return render(req,"course.django.html",{"std_details":student})






