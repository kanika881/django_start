from django.urls import path
from lesson.views import view_form
urlpatterns = [
    path("form/",view_form,name="view_form")
]
