from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def test_api(req):
    return JsonResponse({
        'success':True,
        'domain_auth' : True,
    })