from django.urls import path
from news.views import report_view,reg_success
urlpatterns = [
    path("anchor/",report_view,name="anchor"),
    path("success/",reg_success,name="success")
    
]
