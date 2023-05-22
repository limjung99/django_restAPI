from django.urls import path
from . import views


app_name = "mytodos"
#login url과 APIView를 상속받은 LoginView를 매핑 
urlpatterns = [
    path("login", views.LoginView.as_view(),name="LoginView"),
    path("addtodo",views.AddTodoView.as_view(),name='AddTodoView'),
    path('removetodo',views.RemoveTodoView.as_view(),name='RemoveTodoView')
]