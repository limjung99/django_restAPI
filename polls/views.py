from django.http import HttpResponse,Http404
from .models import Question
from django.template import loader
from django.shortcuts import render,get_object_or_404

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request,"polls/index.html",context)

"""
render를 이용해서 이렇게 짧게도 index view 생성가능 
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
"""

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html",{"question":question})

def results(requst, question_id):
    response = "You are looking at the result of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)

