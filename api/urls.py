from django.urls import path
from django.urls.conf import include
from .views import *
urlpatterns = [
    path('trashcan/',gettc),
    path('town/<str:num>/',getByTown),
    path('trashcan/<str:num>/',getById),
]
