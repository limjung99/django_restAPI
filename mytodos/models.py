from django.db import models
# Create your models here.



#회원테이블 
class Users(models.Model):
    user_id = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=200)
    user_email = models.CharField(max_length=100)
