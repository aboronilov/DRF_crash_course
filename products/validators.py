from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Product


def validate_title_no_hello(value):
    # iexact - без учета регистра
    if "hello" in value.lower():
        raise serializers.ValidationError(f"{value} contains hello")
    return value


unique_validator = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')
