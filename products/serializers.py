from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'content', 'price', 'sale_price', 'details']

    def get_details(self, obj):
        return obj.get_random_info()
