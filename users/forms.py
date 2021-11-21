from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','email','password1','password2']
        labels = {
            'username' : '아이디',
            'first_name':'닉네임',
            'email' : '이메일',
        }
        
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields['password1'].label = '비밀번호'
          self.fields['password2'].label = '비밀번호 확인'   
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['email','nickname']