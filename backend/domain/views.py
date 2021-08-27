from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework.decorators import api_view
from .models import DomainSearched, DomainEnding
from .serializers import DomainSearchedSerializer
import whois

# a simple function, it checks if the user
# has had a previous search history, if he has
# the new domain is just appended in the previous list,
# else a new list is made for the user;


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

# simple function which returns all the domain ending suggestions;


def get_all_domain_endings_list():
    result = []
    from_model = DomainEnding.objects.all()
    for model in from_model:
        result.append(model.name)
    return result


# api for testing if the application is working properly or not;
@api_view(['GET'])
def test_api(req):
    return JsonResponse({
        'success': True,
        'domain': True,
    })


# function which returns the domains that were
# previously searched by the user;
@api_view(['GET'])
def get_history_for_user(req):
    all_history = DomainSearched.objects.filter(user=req.user)
    if (len(all_history) == 0):
        return JsonResponse({
            'success': True,
            'history': {
                'searches': '',
                'sno': '...',
                'user': 'user',
            }
        })
        # serializer which converts the model into readable JSON
    serialized = DomainSearchedSerializer(all_history[0])
    print(serialized.data)

    return JsonResponse({
        'success': True,
        'history': serialized.data
    })

# function which has the logic for getting
# information on the domain searched, and also
# give suggestions to the user for alternatives.


@api_view(['GET'])
def filter_for_query(req, text):
    # getting the first word;
    temp = text.split('.')[0]
    print(type(req.user))
    first_result = whois.whois(text)
    # list containing the suggestions that would be given to the user;
    suggestions = list(map(lambda x: temp + x, get_all_domain_endings_list()))

    # adding the query to user's search history;
    add_domain_to_user_history(text, req.user)
    return JsonResponse({
        'success': True,
        'all_suggestions': suggestions,
        'result': first_result
    })
