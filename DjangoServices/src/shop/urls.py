from django.urls import path
from .views import ShopListAPIView, ShopCreateAPIView, ShopRetrieveDestroyUpdateAPIVIEW

urlpatterns = [
    path('shop-list/', ShopListAPIView.as_view()),
    path('shops/', ShopCreateAPIView.as_view()),
    path('shops/<int:pk>/', ShopRetrieveDestroyUpdateAPIVIEW.as_view()),
]
