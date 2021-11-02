from django.db.models import query
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import ProductSerializer, CollectionSerilizer, ReviewSerializer
from .models import Product, Collection, Review


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['collection_id', 'unit_price']

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
