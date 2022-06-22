from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['pk', 'title', 'content', 'price', 'sale_price', 'details']

    def get_details(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_random_info()
