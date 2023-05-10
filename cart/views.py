from rest_framework.response import Response
from .serializers import CartSerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.models import Product
from django.shortcuts import get_object_or_404


class CartView(ListAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = CartSerializer

    def get_queryset(self):
        cart = self.request.user.cart
        serializer = CartSerializer(cart)
        total_price = 0

        products_data = serializer.data["products_list"]

        for product in products_data:
            total_price += product["price"]

        cart.total = total_price

        return [cart]


class CartAddProductView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        cart = request.user.cart
        seller = product.user_id
        total_price = 0

        cart.products_list.add(product)
        cart.seller_list.add(seller)

        serializer = CartSerializer(cart)
        products_data = serializer.data["products_list"]

        for product in products_data:
            total_price += product["price"]

        cart.total = total_price
        cart.save()

        serializer_cart = CartSerializer(cart)

        return Response(serializer_cart.data, status=201)
