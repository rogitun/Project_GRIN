from os import name
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',home,name='home'),
    path('temp/',search,name='search'),
    path('detail/<str:pk>/',detail,name='detail'),
    #path('api_store/',api_store,name='api_store'),
    path('how/',how,name='how'),
    path('delete/<str:pk>/',deleteReview,name='delete_review'),
    #path('api_store2/',api_store2,name='api_store2'),
]