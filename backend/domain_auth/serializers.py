from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




class MyCustomSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super(MyCustomSerializer,cls).get_token(user)
        token['test'] = "Ningombam is the best"
        return token    