from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(max_length=50,)
    name = serializers.CharField(max_length=50,)
    email = serializers.EmailField(max_length=50,)
    mobile = serializers.CharField(max_length=11)
    state = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('full_name', 'email', 'mobile_number')


class HCPConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model = HCPConnect
        fields = ('__all__')


class WebinarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebinarList
        fields = ('__all__')


class LivewebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livewebinar
        fields = ('__all__')

class ClinicalToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalTool
        fields = ('__all__')

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ('__all__')



    Clinic
