from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework.decorators import api_view
from .models import DomainSearched


def test_api(req):
    return JsonResponse({
        'success': True,
        'domain': True,
    })


@api_view(["GET"])
def check_domain_history(req):
    domain = req.headers.domain
    check = DomainSearched.objects.filter(name=domain)
    return JsonResponse({
        'success': True,
        'empty': (len(check) == 0)
    })


@api_view(['PUT', 'POST'])
def add_history(req):
    if (req.type == 'PUT'):
        domain = req.PUT.domain
        domain_check = DomainSearched.objects.get(name=domain)
        domain_check.searchers.add(req.user)
        domain_check.save()

    else:
        domain = req.POST.domain
        domain_check = DomainSearched(name=domain)
        domain_check.searchers.add(req.user)
        domain_check.save()

    return JsonResponse({
        'success': True,
    })


@api_view(['GET'])
def get_history_for_user(req):
    all_history = DomainSearched.objects.get(searchers__icontains=req.user)
    