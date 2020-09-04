from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import birthday,login

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = '__all__'

class birthdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = birthday
        fields = '__all__'