import logging
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
from .models import Shop
from .serializers import ShopSerializer, ShopListSerializer


process_log = logging.getLogger('process')


class ShopListAPIView(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopListSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ['name', ]
    filterset_fields = ['price']

    def list(self, request, *args, **kwargs):
        process_log.info(f"['shops has been returned successfully!']")
        return super().list(self, request, *args, **kwargs)


class ShopCreateAPIView(generics.CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = []

    def perform_create(self, serializer):
        obj = serializer.save()
        process_log.info(f"['new shop with id {obj.pk} has been added successfully!']")
        return obj


class ShopRetrieveDestroyUpdateAPIVIEW(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = []

    def perform_update(self, serializer):
        process_log.info(f"['update request for shop id {self.kwargs.get('pk')} has been Done successfully!']")
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        process_log.info(f"['delete request for shop id {self.kwargs.get('pk')} has been Done successfully!']")
        return super().perform_destroy(instance)

    def retrieve(self, request, *args, **kwargs):
        process_log.info(f"['retrieve request for shop id {kwargs.get('pk')} has been Done successfully!']")
        return super().retrieve(self, request, *args, **kwargs)
