from django.urls import path
from student.views import stu_info
urlpatterns = [
    path("info/",stu_info)
]
