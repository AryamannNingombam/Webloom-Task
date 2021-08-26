from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import logout
from .models import UserVerified
from django.contrib.auth.models import User
from .mailer import send_mail
from .random_string import get_string
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyCustomSerializer, MyUserSerializer
from rest_framework import permissions


class ObtainTokenPairWithColorView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyCustomSerializer


@api_view(['GET'])
def test_api(req):
    return JsonResponse({
        'success': True,
        'domain_auth': True,
    })


@api_view(['POST'])
@permission_classes((AllowAny,))
def sign_up_user(req):
    email = req.POST.get("email")
    username = req.POST.get('username')
    password = req.POST.get("password")
    first_name = req.POST.get("firstName")
    last_name = req.POST.get('lastName')
    print(req.POST)
    check = User.objects.filter(email=email)
    check2 = User.objects.filter(username=username)
    if (len(check) != 0 or len(check2) != 0):
        return JsonResponse({
            'success': False,
            "message": "User already exists!"
        })
    newUser = User(email=email, username=username, password=password,
                   first_name=first_name,
                   last_name=last_name
                   )
    try:
        newUser.full_clean()
    except Exception as e:
        print(e)
        return HttpResponse(status=500)

    newUser.save()
    rand_string = get_string()
    verified = UserVerified(user=newUser, verified=False,
                            verification_id=rand_string)
    try:
        verified.full_clean()
    except Exception as e:
        return HttpResponse(status=500)
    verified.save()
    send_mail(email, 'http://localhost:8000/api/auth/verify-mail/' +
              rand_string)

    return JsonResponse({
        'success': True,
    })


@ api_view(['POST'])
def sign_out_user(req):
    logout(req.user)
    return JsonResponse({
        'success': True
    })


@ api_view(['GET'])
@permission_classes((AllowAny,))
def verify_mail(req, hash):

    check = UserVerified.objects.filter(verification_id=hash)
    if (len(check) == 0):
        return JsonResponse({
            'success': False,
            'message': "Invalid!"
        })

    ver = check[0]
    ver.verified = True
    ver.save()
    return JsonResponse({
        'success': True
    })


@api_view(['GET'])
def check_user_verified(req, username):
    user_check = User.objects.get(username=username)
    verified_check = UserVerified.objects.get(user=user_check)
    return JsonResponse({
        'success': True,
        'verified': verified_check.verified
    })


@api_view(['GET'])
def get_user_information(req):
    result = MyUserSerializer(req.user)
    print(result.data)
    return JsonResponse({
        'success': True,
        'user_information': result.data
    })
