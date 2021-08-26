from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework.decorators import api_view
from .models import DomainSearched, DomainEnding
from .serializers import DomainSearchedSerializer
import whois


def add_domain_to_user_history(name, user):
    history_check = DomainSearched.objects.filter(user=user)
    # user has searched for the first time;

    if (len(history_check) == 0):
        new_user_history = DomainSearched(user=user)
        new_user_history.searches = f"{name},"
        new_user_history.save()
    # shit already exists;
    else:
        updated_user_history = history_check[0]
        updated_user_history.searches += f"{name},"
        updated_user_history.save()
    return


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
def check_user_history(req):

    check = DomainSearched.objects.filter(user=req.user)
    if (len(check) == 0):
        return JsonResponse({
            'success': True,
            'exists': False,
        })
    else:
        return JsonResponse({
            'success': True,
            'exists': False,
            'user_history': check[0]
        })


@api_view(['GET'])
def get_history_for_user(req):
    all_history = DomainSearched.objects.get(user=req.user)
    serialized = DomainSearchedSerializer(all_history)
    print(serialized.data)

    return JsonResponse({
        'success': True,
        'history': serialized.data
    })


@api_view(['GET'])
def filter_for_query(req, text):
    temp = text.split('.')[0]
    print(type(req.user))
    first_result = whois.whois(text)
    suggestions = list(map(lambda x: temp + x, get_all_domain_endings_list()))
    add_domain_to_user_history(text, req.user)
    return JsonResponse({
        'success': True,
        'all_suggestions': suggestions,
        'result': first_result
    })
