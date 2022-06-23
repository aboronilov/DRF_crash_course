from django.urls import path

from .views import ProductDetailAPIView, ProductListCreateAPIView, ProductUpdateAPIView, ProductDeleteAPIView, \
    ProductMixinView

urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product-edit'),
    path('<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='product-delete'),
    path('', ProductListCreateAPIView.as_view(), name='product-list')
]
