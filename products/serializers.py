from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer
from .models import Product
from .validators import validate_title_no_hello, unique_validator


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(read_only=True, source='user')
    related_products = ProductInlineSerializer(read_only=True, source='user.product_set.all', many=True)
    details = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail")
    title = serializers.CharField(validators=[validate_title_no_hello, unique_validator])
    # email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            # 'email',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'details',
            'related_products'
        ]

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
