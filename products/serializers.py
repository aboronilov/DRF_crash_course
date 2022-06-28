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
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail")
    title = serializers.CharField(validators=[validate_title_no_hello, unique_validator])

    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'public',
        ]

    # можно делать отдельно serializers под каждый метод crud

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if not request:
            return None
        return reverse(viewname="product-edit", kwargs={'pk': obj.pk}, request=request)

