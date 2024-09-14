import json

from django.core import serializers


def serialize(queryset, _fields=None, _type="json"):
    if _fields is not None:
        serialized_data = serializers.serialize(
            _type, queryset, fields=_fields)
    else:
        serialized_data = serializers.serialize(_type, queryset)
    return json.loads(serialized_data)
