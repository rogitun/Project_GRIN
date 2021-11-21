from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register,name='register'),
    path('logout/',logoutUser,name='logout'),
    path('login/',loginUser,name='login')
]
