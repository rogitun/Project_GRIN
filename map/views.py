from django.shortcuts import render,redirect
from os import read
from .models import *
import csv,os
from enum import Enum
from .forms import ReviewForm
# Create your views here.
from django.contrib.staticfiles.storage import staticfiles_storage
from django.templatetags.static import static
class town_num(Enum):
    중로구 = 1
    종로 =1
    중구 = 2
    용산구 = 3
    용산 = 3
    성동구 = 4
    성동 = 4
    광진구 =5
    광진 = 5
    동대문구 =6
    동대문 = 6
    중랑구 = 7
    중랑 = 7
    성북구 = 8
    성북 = 8
    강북구 = 9
    강북 = 9
    도봉구 = 10
    도봉 = 10
    노원구 = 11
    노원 =11
    은평구 = 12
    은평 = 12
    서대문구 = 13
    서대문 =13
    마포구 = 14
    마포 =14
    양천구 = 15
    양천 = 15
    강서구 = 16
    강서 = 16
    구로구 = 17
    구로 =17
    금천구 = 18
    금천 = 18
    영등포구 = 19
    영등포 = 19
    동작구 = 20
    동작 = 20
    관악구 = 21
    관악 =21
    서초구 = 22
    서초 = 22
    강남구 = 23
    강남 =23
    송파구 = 24
    송파 =24
    강동구 = 25
    강동 =25 

def home(request):
    return render(request,'main.html')

def how(request):
    return render(request,'how.html')

def detail(request,pk):
    post = TrashCan.objects.get(tc_id=pk)
    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.post = post
            review.owner = request.user.profile
            review.save()
            return redirect('detail',pk=post.tc_id)
    
    
    return render(request,'detail.html',{"post":post,"form":form,"id":pk})

def deleteReview(request,pk):
    profile = request.user.profile
    review = profile.review_set.get(id=pk)
    key = review.post.tc_id
    
    if request.method == 'POST':
        review.delete()
        return redirect('detail',pk=key)

def search(request):
    search_query=''
    number = 0
    
    if request.GET.get('q'):
        try:
            search_query = request.GET.get('q')
            number = town_num[search_query].value
        except:
            return redirect('home')
               

    return render(request,'sub.html',{"num":number})

#api_store 추가해야함
def api_store(request):
    path= 'static/Test.csv'
    #path= 'C:\\Users\\kunyj\\Desktop\\Django\\SYU_GRIN\\grin\\static\\final1.csv'

    file=open(path)
    reader = csv.reader(file)
    print('-----',reader)
    list = []
    for row in reader:
        list.append(TrashCan(
        tc_town_num=row[0],
        tc_town=row[1],
        tc_road = row[2],
        tc_loc=row[3],
        tc_lat=row[4],
        tc_lng=row[5],
        tc_desc=row[6],
        tc_phone=row[7],
        tc_link=row[8],
        ))
    TrashCan.objects.bulk_create(list)
    return render(request,'api_store.html')

def api_store2(request):
    path= 'staticfiles/Test.csv'
    
    file=open(path)
    reader = csv.reader(file)
    print('-----',reader)
    list = []
    for row in reader:
        list.append(TrashCan(
        tc_town_num=row[0],
        tc_town=row[1],
        tc_road = row[2],
        tc_loc=row[3],
        tc_lat=row[4],
        tc_lng=row[5],
        tc_desc=row[6],
        tc_phone=row[7],
        tc_link=row[8],
        ))
    TrashCan.objects.bulk_create(list)
    return render(request,'api_store.html')
