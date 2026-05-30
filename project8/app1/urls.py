
from django.urls import path
from app1.views import app1_fun

urlpatterns = [
    path("app1_fun/",app1_fun,{"status":"okay"}),
    path("app1_function/",app1_fun),
    
]