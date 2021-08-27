from rest_framework import serializers
from .models import DomainSearched


# serializer to return the search history of the user;
class DomainSearchedSerializer(serializers.ModelSerializer):
    class Meta:
        model =DomainSearched 
        fields = ['sno','user','searches']

