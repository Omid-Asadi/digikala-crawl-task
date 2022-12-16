from django.urls import path
from product.views import ProductListAPIView, ProductCreateAPIView, ProductRetrieveDestroyUpdateAPIVIEW

urlpatterns = [
    path('product-list/', ProductListAPIView.as_view()),
    path('products/', ProductCreateAPIView.as_view()),
    path('products/<int:pk>/', ProductRetrieveDestroyUpdateAPIVIEW.as_view()),
]
