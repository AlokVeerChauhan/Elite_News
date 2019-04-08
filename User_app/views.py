from django.shortcuts import render, redirect
from User_app.forms import UserRoleForm
from User_app.forms import UserRegisterForm
from User_app.models import User_Register
import authorize as au

# Create your views here.
def login(request):
    if(request.method == "POST"):
        uemail = request.POST["email"]
        upass = request.POST["password"]
        #try:
        userdata = User_Register.objects.get(user_email=uemail)
        dp = userdata.user_password
        if(dp == upass):
                request.session['authenticated'] = True
                request.session['role_id'] = userdata.user_role_id_id
                request.session['user_email'] = userdata.user_email
                if(request.session['role_id']==1):
                    redirect("")
        return redirect("/index/")
        #except:
           # return render(request, "login.html", {'invalid': True})
    return render(request, "login.html")



def exmp(request):
    try:
        auth = au.authrizeuser(request.session["authenticated"], request.session["role_id"], 3)
    except:
        return redirect("/notlogin/")
    if (auth==True):

        return render(request, "index.html", {'k1':auth})
    else:
        aut, message = auth
        if(message=="Wrong User"):
            return redirect("/wronguser/")
        elif(message=="Not Login"):
            return redirect("/notlogin/")

def logout(request):
    request.session['authenticated'] = False
    return redirect("/login/")

def index(request):
    return render(request, "index.html")

def business(request):
    return render(request, "business.html")

def entertainment(request):
    return render(request, "entertainment.html")

def lifestyle(request):
    return render(request, "lifestyle.html")

#def login(request):
    #return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def sports(request):
    return render(request, "sports.html")

def technology(request):
    return render(request, "technology.html")

def world(request):
    return render(request, "world.html")


