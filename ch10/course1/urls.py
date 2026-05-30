from django.urls import path
from course1.views import learn_python

urlpatterns = [
    path("ruby",learn_python)
]
