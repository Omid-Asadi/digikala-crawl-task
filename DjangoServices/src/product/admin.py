from django.contrib import admin
from product.models import Product
from shop.models import Shop


admin.site.register(Shop)
admin.site.register(Product)
