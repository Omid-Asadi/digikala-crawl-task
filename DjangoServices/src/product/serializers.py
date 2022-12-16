from rest_framework import serializers
from product.models import Product
from shop.serializers import ShopSerializer


class ProductSerializer(serializers.ModelSerializer):
    shops = ShopSerializer(many=True)

    class Meta:
        model = Product
        fields = ("pk", "jalali_created_time", "brand", "minimum_market_price", "capacity", "shops")


class ProductCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("pk", "brand", "minimum_market_price", "capacity", "shops")


class ProductLightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("pk", "brand", )
