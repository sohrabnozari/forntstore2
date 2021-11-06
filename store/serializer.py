import collections
from rest_framework import serializers
from decimal import Decimal
from .models import Cart, CartItem, Collection, Product, Review


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'inventory',
                  'unit_price', 'price_with_tax', 'collection']
    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    def calculate_tax(self, product=Product):
        return product.unit_price * Decimal(1.1)


class CollectionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'featured_product', 'collection_population']
    collection_population = serializers.SerializerMethodField(
        method_name='calaculate_collection_population')

    def calaculate_collection_population(self, collection=Collection):
        return collection.collection.count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)


class CartSerializer(serializers.ModelSerializer):
    # id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Cart
        fields = ['id']


# class CartItemSerializer(serializers.Serializer):
#     class Meta:
#         models: CartItem
#         fields: ['cart', 'product', 'quantitiy']
