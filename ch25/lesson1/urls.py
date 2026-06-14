from django.urls import path
from lesson1.views import reg_view
urlpatterns = [
    path("register/",reg_view,name="reg")
]
