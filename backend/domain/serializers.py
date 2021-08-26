from rest_framework import serializers
from .models import DomainSearched


class DomainSearchedSerializer(serializers.ModelSerializer):
    class Meta:
        model =DomainSearched 
        fields = ['sno','user','searches']

