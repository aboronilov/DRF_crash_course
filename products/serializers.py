from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title_no_hello, unique_validator


class ProductSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail")
    title = serializers.CharField(validators=[validate_title_no_hello, unique_validator])
    # name = serializers.CharField(read_only=True, source='title')

    class Meta:
        model = Product
        fields = [
            'url',
            'edit_url',
            # 'name',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'details'
        ]

    # я не мерджил

    # можно делать отдельно serializers под каждый метод crud
    # def create(self, validated_data):
    #     email = validated_data.pop('email')
    #     super().create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     super().update(instance, validated_data)

    # def validate_title(self, value):
    #     # iexact - без учета регистра
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if not request:
            return None
        return reverse(viewname="product-edit", kwargs={'pk': obj.pk}, request=request)

    def get_details(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_random_info()
