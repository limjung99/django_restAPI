
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UsersSerializer
from django.http import HttpResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Users
# Create your views here.

# Login을 담당 view <- API view를 상속받는 class형 view (basci Django view는 함수)
# view는 요청에 대한 결과로 HttpResponse를 반환 
class LoginView(APIView):

    def post(self,request):
        serializer = UsersSerializer(data = request.data)
        if serializer.is_valid(): # post로 전송받은 data의 유효성 검사 
            #직렬화된 유효한 data를 validated_data 메소드로 가져온다. 
            id = serializer.validated_data['user_id']
            pw = serializer.validated_data['user_pw']
            # DB에 일치하는 tuple이 존재하는지검사 
            if serializer.validate(request.data):
                #simple-jwt 
                user = Users.objects.filter(user_id=id,user_pw=pw)
                token = TokenObtainPairSerializer.get_token(user)
                refresh_token = str(token)
                access_token = str(token.access_token)

                return Response({
                    "jwt_token" : {
                        "refresh_token" : refresh_token,
                        "access_token" : access_token
                    }
                })
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def get_token(self,user_id):
        refresh = RefreshToken.for_user(user_id)
        tokens = {
            'refresh':str(refresh),
            'access':str(refresh.access_token),
        }
        return tokens




    