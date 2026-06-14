from django.urls import path
from lesson.views import reg_view
urlpatterns = [
    path("lesson/",reg_view,name="reg")
]
