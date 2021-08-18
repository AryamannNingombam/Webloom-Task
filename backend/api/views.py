from django.http import JsonResponse
from rest_framework.decorators import api_view
import whois
import json

@api_view(["GET", "POST"])
def test_api(request):
    if (request.method == "POST"):
        url = json.loads(request.body.decode("utf-8"))['url']
        result = whois.whois(url)

 
        return JsonResponse({
            'success': True,
            'i_am_great': True,
            'result' : result
        })

    return JsonResponse({
        'success': True,
        'i_am_great': True,
    })
