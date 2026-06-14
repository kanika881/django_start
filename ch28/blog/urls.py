from django.urls import path,register_converter
from blog.views import hp,article,year_page
from blog.converters import FourDigitYearConvertor

register_converter(FourDigitYearConvertor,'yyyy')
urlpatterns = [
    path("",hp,name="home"),
    path("article/",article,name="art"),
    # path("article/year/<int:my_year>",year_page,name="year")
    # path("article/year/<str:my_year>",year_page,name="year")
    # path("article/year/<slug:my_year>",year_page,name="year")
    # path("article/year/<int:my_year>/<int:month>",year_page,name="year")
    path("article/year/<yyyy:my_year>/<int:month>",year_page,name="year")
    
    
    
]
