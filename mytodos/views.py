
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
            # DB에 일치하는 tuple이 존재하는지검사 
            if serializer.validate(request.data):
                #DB에 존재하는 tuple이므로 token을 발급해준다

                #직렬화된 유효한 data를 validated_data 메소드로 가져온다. 
                id = serializer.validated_data['user_id']
                pw = serializer.validated_data['user_pw']
                #filter를 통해 iterable한 tuple collection을 가져온다 , index로도 접근가능.
                users = Users.objects.filter(user_id=id,user_pw=pw)
                user = users[0]
                #token생성 로직 
                token = TokenObtainPairSerializer.get_token(user)
                refresh_token = str(token)
                access_token = str(token.access_token)
                res = Response({
                    "token":{
                        "access":access_token,
                        "refresh":refresh_token,
                    },
                },status=status.HTTP_200_OK)
                res.set_cookie("access",access_token,httponly=True)
                res.set_cookie("refresh",refresh_token,httponly=True)

                return res
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def get_token(self,user_id):
        refresh = RefreshToken.for_user(user_id)
        tokens = {
            'refresh':str(refresh),
            'access':str(refresh.access_token),
        }
        return tokens




    