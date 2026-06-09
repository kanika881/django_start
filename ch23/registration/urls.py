from django.urls import path
from registration.views import log_view
urlpatterns = [
    path("log/",log_view)
]
