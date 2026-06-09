from django.shortcuts import render
from learn.form import reg,log

def reg_view(req):
    # fm=reg(auto_id=True)
    # fm=reg(auto_id="id_%s")
    # fm=reg(auto_id=False)
    fm=reg(auto_id=True,field_order=["phone_no"],initial={"phone_no":"00XXX","age":"0"})
    return render(req,"learn/resgiter.html",{"form":fm})

# Create your views here.
def log_view(req):
    fm=log()
    return render(req,"learn/login_for.html",{"form":fm})

    