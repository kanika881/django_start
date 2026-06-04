from django.urls import path 
from student.views import all,single
urlpatterns = [
    path("data/",all),
    path("single",single)
]
