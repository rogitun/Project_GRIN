from django.contrib.auth.models import *
from django.db.models import fields
from map.models import *
from rest_framework import serializers

class TrashSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashCan
        fields = '__all__'

