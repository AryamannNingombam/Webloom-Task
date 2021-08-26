from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers




class MyCustomSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super(MyCustomSerializer,cls).get_token(user)
        token['test'] = "Ningombam is the best"
        return token    

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','username','first_name','last_name']