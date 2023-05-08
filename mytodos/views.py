
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UsersSerializer
# Create your views here.

# Login을 담당 view 
class LoginView(APIView):

    def post(self,request):
        serializer = UsersSerializer(data = request.data)
        print(request.data)
        if serializer.is_valid(): # post로 전송받은 data의 유효성 검사 
            #직렬화된 유효한 data를 validated_data 메소드로 가져온다. 
            id = serializer.validated_data['user_id']
            pw = serializer.validated_data['user_pw']
            
            if serializer.validate(request.data):
                return request.data
            else:
                return "bye"
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



    