from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    #꺾쇠부분은 capture되어 view의 arg와 일치하는 패턴을 식별한다
    #즉 view의 인수가 question_id와 일치하는 패턴을 식별하여 매칭되는 view를 호출
    # 예를들어 'polls/숫자/' 엔드포인트를 detail과 매핑시켜준다
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/",views.DetailView.as_view(),name="detail"),
    path("<int:pk>/results/",views.ResultsView.as_view(),name="results"),
    path("<int:question_id>/vote/",views.vote,name="vote"),
]