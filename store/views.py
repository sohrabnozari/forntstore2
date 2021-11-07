from django.db.models import query
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from .filters import ProductFilter
from .serializer import CartSerializer, ProductSerializer, CollectionSerilizer, ReviewSerializer
from .models import Product, Collection, Review, Cart


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['collection_id', 'unit_price']
    # SearchFilter = ['title', 'description']
    filterset_class = ProductFilter  # --> doesn't work properly

    def get_serializer_context(self):
        return {'request': self.request}
    # ---------------------------------------------------------------------------------------


class CollectionViewSet(ModelViewSet):

    queryset = Collection.objects.all()
    serializer_class = CollectionSerilizer

    def delete(self, request, pk):

        collection = get_object_or_404(Collection, pk=pk)
        if collection.collection.count() > 0:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# -------------------------------------------------------------------------------------------


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}

# ----------------------------------------------------------------------------


class CartViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer
