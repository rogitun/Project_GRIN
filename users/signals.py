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
        - 지도에서 현재 위치를 확인해 주변 쓰레기통을 확인하세요
        2. 댓글
        - 댓글을 통해 쓰레기통 상황에 관한 다양한 의견을 남겨주세요
        3. 분리수거 방법
        - 분리수거 방법을 확인해 올바른 분리배출을 실천해주세요
        4.유의사항
        - 본 서비스는 삼육대학교 SW프로젝트 경진대회를 위해 제작되었습니다.
        시연용으로 배포하였기 때문에 서버 속도가 빠르지 않은 점 양해 부탁드립니다.
        - 본 서비스는 서울시에서 제공한 서울시 가로휴지통의 설치현황을 참고하여 제작되었으며
        정확하지 않은 주소는 주소의 상세 정보 페이지에 나타나 있는 해당 구청의 청소행정과로 민원을 제기하거나 저희에게 알려주시면
        수정하도록 하겠습니다.
        - 주소에서 ID(XX-XXX)가 포함된 주소는 버스정류장의 번호를 의미합니다.
        
        
        개발자 : [김소희, 유다빈, 주미진, 황한슬]
        '''
        send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [profile.email],
        fail_silently=False,
        )
    
        

post_save.connect(create,sender=User)
