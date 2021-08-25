from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework.decorators import api_view
from .models import DomainSearched, DomainEnding
from .serializers import DomainSearchedSerializer
import whois




def add_user_to_domain_searched(name, user):
    domain_searched = DomainSearched.objects.filter(name=name)
    # the first time the domain has been searched for;
    if (len(domain_searched) == 0):
        new_domain_searched = DomainSearched(name=name)
        new_domain_searched.save()
        new_domain_searched.searchers.add(user)
        new_domain_searched.save()
    else:
        domain_searched[0].searchers.add(user)
        domain_searched[0].save()


def get_all_domain_endings_list():
    result = []
    from_model = DomainEnding.objects.all()
    for model in from_model:
        result.append(model.name)
    return result


@api_view(["GET"])
def get_domain_information(req):
    domain = req.GET.get('domain')
    response = whois.whois(domain)
    return JsonResponse({
        'success': True,
        'domain_info': response
    })


@api_view(['GET'])
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
    serialized = DomainSearchedSerializer(all_history, many=True)

    return JsonResponse({
        'success': True,
        'history': serialized
    })


@api_view(['GET'])
def filter_for_query(req, text):
    temp = text.split('.')[0]
    print(type(req.user))
    first_result = whois.whois(text)
    suggestions = list(map(lambda x: temp + x, get_all_domain_endings_list()))
    add_user_to_domain_searched(text,req.user)
    return JsonResponse({
        'success': True,
        'all_suggestions': suggestions,
        'result': first_result
    })
