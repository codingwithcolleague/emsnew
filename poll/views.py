from random import choice
from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Answer, Question
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    context = {}
    context["questions"] = Question.objects.all()
    context["title"] = "poll"
    print(context)
    return render(request,"poll/index.html",context)

def details(request,id=None):
    context = {}
    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404("Details not found")
    context["question"] = question
    return render(request,"poll/details.html", context)

def poll(request,id=None):
    if request.method == "GET":
        try:
            question = Question.objects.get(id=id)
        except:
            raise Http404("Not Found")
        context = {}
        context["question"] = question
        return render(request,"poll/poll.html" , context)
    
    if request.method == "POST":
        user_id = request.user.id
        data = request.POST
        ret = Answer.objects.create(user_id=user_id,choice_id=data['choice'])
        if ret:
            return HttpResponse("your vote is given")
        else:
            return HttpResponse("your vote is not done successfylly")

def polldetails(request,id):
    context = {}
    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404("Details not found")
    context["question"] = question
    return render(request,"poll/polldetails.html",context)