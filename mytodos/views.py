
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Max

from django.http import HttpResponse
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Users,Todos
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import JSONParser



#Login
class LoginView(APIView):

    def post(self,request): 
        data = request.data
        
        userId = data['user_id']

        try:
            obj = Users.objects.get(user_id=userId)
        except:
            return Response(status=400)
        
        if data['user_pw'] == obj.user_pw:
            #login성공 
            todoObjs = Todos.objects.filter(user=obj)
            todos = ""

            for todoObj in todoObjs:
                todos += todoObj.content+","
            
            return Response({ 'todos' : todos },status=200) 
        else:
            return Response(status=400) 
        
        
    

class AddTodoView(APIView):
    
    def post(self,request):
        newTodoText = request.data['todo']
        userId = request.data['user_id']
        obj = Users.objects.get(user_id=userId)
        max_value = Todos.objects.aggregate(max_value=Max('content_id'))['max_value']
        newTodoObj = Todos(user=obj,content=newTodoText,content_id=max_value+1)
        newTodoObj.save()

        return Response(status=200)


class RemoveTodoView(APIView):
    def post(self,request):
        removeTodoText = request.data['removeTodo']
        Todos.objects.filter(content=removeTodoText).delete()
        return Response(status=200)

    