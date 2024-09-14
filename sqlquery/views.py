import json

from django.core.serializers import serialize
from django.http import JsonResponse

from .models import Product


def home(request):
    qs = Product.objects.all()
    serialized_data = serialize("json", qs)
    serialized_data = json.loads(serialized_data)
    return JsonResponse(serialized_data, safe=False,  status=200)
