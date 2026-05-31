from django.urls import path
from courses.views import learn_django,learn_python
urlpatterns = [
    path("py/", learn_python),
    path("dj/",learn_django)
]
