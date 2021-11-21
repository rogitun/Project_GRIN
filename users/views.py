from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def register(request):
    page = 'register'
    form = CustomUserCreationForm()
    msg = ""
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form['password1'].value() != form['password2'].value():
            msg = "비밀번호가 일치하지 않습니다."    
        elif not User.objects.filter(email=form['email'].value()):
            if User.objects.filter(username=form['username'].value()):
                msg = "이미 가입된 유저입니다."
            elif form.is_valid():
                user = form.save(commit=False)        
                user.username = user.username.lower()
                user.save()
                login(request,user)
                return redirect('home')
            else:
                msg = "비밀번호를 더 안전하게 설정해주세요. 한영 혼용 및 8자 이상."
        else:
            msg="이미 가입된 이메일 입니다."
    context = {'form':form,'page':page,'msg':msg}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def loginUser(request):
    page = 'login'
    msg = ""
    if request.user.is_authenticated:
        return redirect('home')
    if request.method =='POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            msg = "존재하지 않는 아이디 입니다."
            return render(request,'login.html',{"msg":msg})
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            msg = "비밀번호가 일치하지 않습니다."
        
    return render(request,'login.html',{"msg":msg})