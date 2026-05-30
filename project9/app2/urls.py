from django.urls import path
from app2.views import maths_learn

urlpatterns = [
   
    path("app2/",maths_learn)
    
]
