from django.db import models
# Create your models here.

#회원테이블 
class Users(models.Model):
    user_id = models.CharField(max_length=20,primary_key=True)
    user_pw = models.CharField(max_length=200)
    

class Todos(models.Model):
    user = models.ForeignKey('Users',related_name='POST',on_delete=models.CASCADE)
    content = models.CharField(max_length=200,)
    content_id = models.IntegerField(primary_key=True)
