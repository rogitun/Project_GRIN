from django.db import models
from users.models import Profile

class TrashCan(models.Model):
    tc_id=models.IntegerField(primary_key=True)
    tc_town_num=models.IntegerField(null=True)
    tc_town=models.CharField(null=True,max_length=32,default="NoInput")
    tc_road=models.CharField(null=True,max_length=128,default="NoInput")
    tc_loc=models.CharField(null=True,max_length=128,default="NoInput")
    tc_lat=models.CharField(null=True,max_length=100)
    tc_lng=models.CharField(null=True,max_length=100)
    tc_desc=models.CharField(null=True,max_length=256,default="NoInput")
    tc_phone=models.CharField(null=True,max_length=48)
    tc_link = models.URLField(max_length=128,blank=True,null=True)
    def __str__(self):
        return self.tc_loc
    
class Review(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    post = models.ForeignKey(TrashCan,on_delete=models.CASCADE)
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.IntegerField(primary_key=True) 
    
    def __str__(self):
        return self.body