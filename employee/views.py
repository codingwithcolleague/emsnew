from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from ems.decorator import role_required,admin_only

@login_required(login_url='/auth/login/')
def employee_list(request):
    print(request.role)
    context = {}
    context['users'] = User.objects.all()
    context['title'] = 'Employees' 
    return render(request,"employee/index.html",context)

def employee_details(request,id):
    context = {}
    context['user'] = get_object_or_404(User,id=id)
    return render(request,"employee/details.html" , context)

@login_required(login_url='/auth/login/')
# @role_required(allowed_roles=['HR','Admin'])
@admin_only
def employee_add(request):
    context = {}
    form = UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        form.save()
        # userdata = User.objects.create(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
        # if userdata:
        return redirect("employee:list")
    context['form'] = form
    return render(request,"employee/add.html",context)

def employee_edit(request,id):
    user = get_object_or_404(User,id=id)
    if request.method == "POST":
        user_form = UserForm(request.POST,instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect("employee:list")
    else:
        user = UserForm(instance=user)
    context = {}
    context['form'] = user
    return render(request,"employee/add.html",context)


def employee_delete(request,id):
    user = get_object_or_404(User,id=id)
    user.delete()
    return redirect("employee:list")