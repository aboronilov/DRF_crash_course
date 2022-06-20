from django.urls import path

from .views import ProductDetailAPIView, ProductListCreateAPIView, ProductUpdateAPIView, ProductDeleteAPIView, \
    ProductMixinView

urlpatterns = [
    path('<int:pk>/', ProductMixinView.as_view()),
    path('<int:pk>/update/', ProductMixinView.as_view()),
    path('<int:pk>/delete/', ProductMixinView.as_view()),
    path('', ProductMixinView.as_view())
]
