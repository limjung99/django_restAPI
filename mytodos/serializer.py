from .models import Users
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id','user_pw')

    def validate(self, args):
        id = args.get('user_id')
        pw = args.get('user_pw')

        if id and pw:
            try:
                user = Users.objects.get(user_id=id)
                if user.user_pw != pw: #login정보 없음 
                    raise serializers.ValidationError('ID와 Password가 일치하지 않습니다.')
            except Users.DoesNotExist:
                raise serializers.ValidationError('일치하는 정보가 존재하지 않습니다.')
            return args