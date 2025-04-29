from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(
        description="Retrieve a list of all products",
        responses={200: ProductSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        """Retrieve a list of all products"""
        return super().list(request, *args, **kwargs)

    @extend_schema(
        description="Create a new product",
        request=ProductSerializer,
        responses={201: ProductSerializer},
    )
    def create(self, request, *args, **kwargs):
        """Create a new product"""
        return super().create(request, *args, **kwargs)

    @extend_schema(
        description="Retrieve a product by ID",
        responses={200: ProductSerializer},
    )
    def retrieve(self, request, *args, **kwargs):
        """Retrieve a product by ID"""
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        description="Update a product by ID",
        request=ProductSerializer,
        responses={200: ProductSerializer},
    )
    def update(self, request, *args, **kwargs):
        """Update a product by ID"""
        return super().update(request, *args, **kwargs)

    @extend_schema(
        description="Partially update a product by ID",
        request=ProductSerializer,
        responses={200: ProductSerializer},
    )
    def partial_update(self, request, *args, **kwargs):
        """Partially update a product by ID"""
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        description="Delete a product by ID",
        responses={204: 'Product deleted'},
    )
    def destroy(self, request, *args, **kwargs):
        """Delete a product by ID"""
        return super().destroy(request, *args, **kwargs)
