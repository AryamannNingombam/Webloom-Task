from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth import login, logout, authenticate
from .models import UserVerified
from django.contrib.auth.models import User
from .mailer import send_mail
from .random_string import get_string
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyCustomSerializer
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
def sign_up_user(req):
    email = req.POST.get("email")
    username = req.POST.get('username')
    password = req.POST.get("password")
    first_name = req.POST.get("firstName")
    last_name = req.POST.get('lastName')
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

    newUser.save()
    rand_string = get_string()
    verified = UserVerified(user=newUser, verified=False,
                            verification_id=rand_string)
    verified.save()
    send_mail(email, 'https://localhost/api/auth/verify-mail/' +
              rand_string + '/')

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
def verify_mail(req):
    _id = req.params.get('id')

    check = UserVerified.objects.filter(verification_id=_id)
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
        'success': False,
        'verified': verified_check.verified
    })
