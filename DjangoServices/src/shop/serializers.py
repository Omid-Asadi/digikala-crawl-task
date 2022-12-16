from rest_framework import serializers
from shop.models import Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ("pk", "jalali_created_time", "name", "price", "product")


class ShopListSerializer(serializers.ModelSerializer):
    from product.serializers import ProductLightSerializer
    product = ProductLightSerializer()

    class Meta:
        model = Shop
        fields = ("pk", "jalali_created_time", "name", "price", "product")