from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    #꺾쇠부분은 capture되어 view의 arg와 일치하는 패턴을 식별한다
    #즉 view의 인수가 question_id와 일치하는 패턴을 식별하여 매칭되는 view를 호출
    # 예를들어 'polls/숫자/' 엔드포인트를 detail과 매핑시켜준다
    path("", views.index, name="index"),
    path("<int:question_id>/",views.detail,name="detail"),
    path("<int:question_id>/results/",views.results,name="results"),
    path("<int:question_id>/vote/",views.vote,name="vote"),
]