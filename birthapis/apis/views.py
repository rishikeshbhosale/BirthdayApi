from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import login, birthday
from .serializers import loginSerializer, birthdaySerializer
from rest_framework import status


# Create your views here.
class loginList(APIView):
    def get(self, request):
        logins = login.objects.all()
        serializer = loginSerializer(logins, many=True)
        return Response(serializer.data)

    def post(self, request):
        logins = login.objects.all()
        serializer = loginSerializer(logins, many=True)
        return Response(serializer.data)


class birthdayList(APIView):
    def get(self, request):
        birthdays = birthday.objects.all()
        serializer = birthdaySerializer(birthdays, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        birthdays = birthday.objects.all()
        serializer = birthdaySerializer(birthdays, many=True)
        return Response(serializer.data)

class birthdayDOB(APIView):
    def get(self, request,dt):
        print(dt)
        try:
            birthdays = birthday.objects.filter(DOB__contains=dt)
            print(birthday)
        except:
            return Response("No birthdays ", status=status.HTTP_404_NOT_FOUND)
        serializer = birthdaySerializer(birthdays, many=True)
        return Response(serializer.data)