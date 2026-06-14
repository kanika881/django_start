from django.urls import path
from my_app.views import my_form_view

urlpatterns = [
    path("form/",my_form_view,name="my")
]
