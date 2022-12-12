import logging
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer, ProductCreateUpdateSerializer
from rest_framework import filters


process_log = logging.getLogger('process')


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ['brand', ]

    def list(self, request, *args, **kwargs):
        process_log.info(f"['products has been returned successfully!']")
        return super().list(self, request, *args, **kwargs)


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateSerializer
    permission_classes = []

    def perform_create(self, serializer):
        obj = serializer.save()
        process_log.info(f"['new product with id {obj.pk} has been added successfully!']")
        return obj


class ProductRetrieveDestroyUpdateAPIVIEW(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []
    search_fields = ['brand', ]
    filterset_fields = ['capacity', 'price', 'brand']

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return ProductCreateUpdateSerializer
        return super().get_serializer_class()

    def perform_update(self, serializer):
        process_log.info(f"['update request for product id {self.kwargs.get('pk')} has been Done successfully!']")
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        process_log.info(f"['delete request for product id {self.kwargs.get('pk')} has been Done successfully!']")
        return super().perform_destroy(instance)

    def retrieve(self, request, *args, **kwargs):
        process_log.info(f"['retrieve request for product id {kwargs.get('pk')} has been Done successfully!']")
        return super().retrieve(self, request, *args, **kwargs)
