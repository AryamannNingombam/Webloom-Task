from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework.decorators import api_view
from .models import DomainSearched, DomainEnding
from .serializers import DomainSearchedSerializer
import whois


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
def filter_for_query(req):
    text = req.GET.get('text')
    temp = text.split('.')[0]
    first_result = whois.whois(text)
    all_domain_suggestions = map(
        lambda x:  temp+x, get_all_domain_endings_list())
    final_result = [first_result]
    for domain_suggestion in all_domain_suggestions:
        final_result.append(whois.whois(domain_suggestion))

    return JsonResponse({
        'success': True,
        'all_suggestions': final_result
    })
