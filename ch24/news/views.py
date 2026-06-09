from django.shortcuts import render
from news.forms import report
from django.http import HttpResponseRedirect

def report_view(req):
    # IT GIVES Error 
    fm=report()
    # if req.method=="POST":
    #     print(req.POST["Name_anchor"])
    # else:
    #     fm=report()
    if req.method =="POST":
        fm=report(req.POST)
        if fm.is_valid():
            A_name=fm.cleaned_data["Name_anchor"]
            Domain=fm.cleaned_data["Domain"]
            experience=fm.cleaned_data["year_experience"]
            print({"Anchor_Name:":A_name,"Domain":Domain,"experince":experience})
            # fm=report()  #is se data chala jyga but if someone resbumit then vapis data resubmit hojyga 
            # return HttpResponseRedirect("/reporter/success")
            return HttpResponseRedirect("/reporter/anchor")
        else:
            fm=report()
            
    return render(req,'news/anchor.html',{"form":fm})
# to overcome redirection 
    
def reg_success(req):
    return render(req,"news/success.html")
