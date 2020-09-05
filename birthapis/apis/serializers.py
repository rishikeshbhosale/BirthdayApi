from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import birthday, login, worklocation, designation

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = '__all__'

class birthdaySerializer(serializers.ModelSerializer):
    eDesignation = serializers.SlugRelatedField(read_only=True, slug_field='designation')
    workLocation = serializers.SlugRelatedField(read_only=True, slug_field='location')
    class Meta:
        model = birthday
        fields = '__all__'

class worklocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = worklocation
        fields = '__all__'

class designationSerializer(serializers.ModelSerializer):
    class Meta:
        model = designation
        fields = '__all__'