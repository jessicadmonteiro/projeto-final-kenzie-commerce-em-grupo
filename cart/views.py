from .models import Cart
from rest_framework.response import Response
from .serializers import CartSerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.models import Product
from django.shortcuts import get_object_or_404


class CartView(ListAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

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




