from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse

from .decorators import log_queries
from .models import Product
from .utils import serialize


@log_queries
def home(request):
    qs1 = Product.objects.all()
    qs2 = User.objects.all()

    serialized_data1 = serialize(qs1)
    serialized_data2 = serialize(
        qs2, _fields=['username', 'email', 'last_login', 'is_active'])
    return JsonResponse({
        "products": serialized_data1,
        "users": serialized_data2
    }, safe=False,  status=200)


@ log_queries
def products(request):
    qs = Product.objects.all()
    serialized_data = serialize(qs)
    return JsonResponse(serialized_data, safe=False,  status=200)


@ log_queries
def users(request):
    qs = User.objects.all()
    serialized_data = serialize(
        qs, _fields=['username', 'email', 'last_login', 'is_active'])
    return JsonResponse(serialized_data, safe=False, status=200)


def html_template(request):
    html_str = """
    <div>
        <h1>Hello, Welcome to Django 5.1</h1>
        <hr/>
        <p>Following APIs are available for public access:- </p>
        <ul>
            <p>
                <li>
                    <a href="/home">/home</a>
                </li>
            </p>
            <p>
                <li>
                    <a href="/products/">/products</a>
                </li>
            </p>
            <p>
                <li>
                    <a href="/users">/users</a>
                </li>
            </p>
            <p>
                <li>
                    <a href="/duplicates">/duplicates</a>
                </li>
            </p>
        </ul>
    </div>
    """
    return HttpResponse(html_str)


@log_queries
def duplicates(request):
    qs1 = Product.objects.all()
    _ = serialize(qs1)
    qs2 = Product.objects.all()
    _ = serialize(qs2)
    return JsonResponse({"message": "Testing duplicate Queries"}, status=200)
