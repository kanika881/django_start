from django.urls import path
from app2.views import learn_pandas

urlpatterns = [
    path('pandas/',learn_pandas,{"fees":"200"})
]
