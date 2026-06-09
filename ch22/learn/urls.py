from django.urls import path
from learn.views import reg_view,log_view
urlpatterns = [
    path("reg/",reg_view),
    path("log/",log_view)
    
]
