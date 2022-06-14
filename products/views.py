from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        serializer.save()


class ProductListAPIView(generics.ListAPIView):
    """
    Не использую так как есть
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
