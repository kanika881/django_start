from django.urls import path
from course.views import learn_django,learn_python
urlpatterns = [
    path("py/",learn_python,name="py"),
    path("dj/",learn_django,name="dj")
    
]
