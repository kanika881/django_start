from django.shortcuts import render


def hp(req):
    return render(req,"blog/home.html")

def article(req):
    return render(req,"blog/articles.html")

def year_page(req,my_year,month):
    year={"id":my_year,"month":month}
    return render(req,"blog/year.html",context=year)

# Create your views here.
