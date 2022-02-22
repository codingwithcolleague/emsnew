from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render,reverse
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def employee_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user  = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            if request.GET.get("next" , None):
                print("helllooooooo")
                return HttpResponseRedirect(request.GET['next'])
            return redirect("/success")
        else:
            context["error"] = "Password is not correct"
 
    return render(request,"auth/login.html",context)


def usersuccess(request):
    context = {}
    context['user'] = request.user
    return render(request,"auth/success.html",context)


def employee_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("auth:login")