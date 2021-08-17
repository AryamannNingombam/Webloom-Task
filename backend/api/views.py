from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(["GET"])
def test_api(request):
    return JsonResponse({
        'success': True,
        'i_am_great': True,
    })
