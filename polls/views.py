from typing import Any
from django.db import models
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Question
from django.template import loader
from django.shortcuts import render,get_object_or_404
from .models import Choice, Question
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# listview는 개체 목록 표시를 추상화
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

# detailview는 특정 개체 유형에 대한 세부 정보 페이지 표시를 추상화
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    
    # 현재 시점 이하만 나타나도록 필터링 
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name ="polls/reusults.html"


def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError,Choice.DoesNotExist):
        return render(request,
                      "polls/detail.html",
                      {
                          "question":question,
                          "error_message":"You didn't select a choice.",
                      }
                      )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #result페이지로 리다이렉트
        return HttpResponseRedirect(reverse("polls:results",args=(question_id,)))



