from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings


def create(sender,instance,created,**kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            nickname = user.first_name,
            email = user.email,
        )
        subject = "Grin에 참여해주셔서 감사합니다!"
        message = '''
        깨끗한 거리를 위한 발걸음 감사합니다!
        더 이상 쓰레기통을 찾아 헤매지 마세요!
        Grin 활용하기
        1. 지도
        지도에서 현재 위치를 확인해 주변 쓰레기통을 확인하세요
        2. 댓글
        댓글을 통해 쓰레기통 상황에 관한 다양한 의견을 남겨주세요
        3. 분리수거 방법
        분리수거 방법을 확인해 올바른 분리배출을 실천해주세요
        유의사항
        쓰레기통이 더러울 경우에 서울시민을 위해 댓글을 남겨주세요!!
        
        개발자: 김소희, 유다빈, 주미진, 황한슬
        '''
        send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [profile.email],
        fail_silently=False,
        )
    
        

post_save.connect(create,sender=User)
