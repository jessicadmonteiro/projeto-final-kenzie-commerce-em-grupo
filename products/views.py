from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.permissions import IsAuthenticatedOrReadOnly


class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = ProductSerializer

    def get_queryset(self):
        name = self.request.query_params.get("name")
        category = self.request.query_params.get("category")
        product_id = self.request.query_params.get("id")
        if name:
            return Product.objects.filter(name__icontains=name)
        if category:
            return Product.objects.filter(category__icontains=category)
        if product_id:
            return Product.objects.filter(id=product_id)
        return Product.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
