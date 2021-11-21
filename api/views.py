from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response, responses
from .serializers import *
from map.models import *

@api_view(['GET'])
def gettc(request):
    tcs = TrashCan.objects.all()
    serializer = TrashSerializer(tcs,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getByTown(request,num):
    tc = TrashCan.objects.filter(tc_town_num=num)
    serializer = TrashSerializer(tc,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getById(request,num):
    tc = TrashCan.objects.get(id=num)
    serializer = TrashSerializer(tc,many=False)
    return Response(serializer.data)