from django.urls import path
from core.views import learn_django

urlpatterns = [
    path("dj/",learn_django)
]
