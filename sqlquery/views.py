import json

from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import JsonResponse

from .models import Product
from .utils import log_queries


@log_queries
def home(request):
    qs = Product.objects.all()
    # qsn = User.objects.all()
    serialized_data = serialize("json", qs)
    serialized_data = json.loads(serialized_data)
    return JsonResponse(serialized_data, safe=False,  status=200)
