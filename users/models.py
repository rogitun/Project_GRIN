from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=500,blank=True,null=True)
    nickname = models.CharField(max_length=100,null=True,default="서울시민")

    def __str__(self):
        return self.email