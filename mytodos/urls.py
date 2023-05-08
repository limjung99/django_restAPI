from django.urls import path
from . import views


app_name = "mytodos"
urlpatterns = [
    path("login", views.LoginView.as_view(),name="LoginView"),
]