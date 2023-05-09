from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import Order
from cart.models import Cart
from user.models import User
from products.models import Product
from .serializers import OrderSerializer
from cart.serializers import CartSerializer 
from rest_framework.generics import ListCreateAPIView


class OrderView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        cart = request.user.cart
        products = cart.products_list.all()
        sellers = cart.seller_list.all()

        for seller in sellers:
            seller = seller.id
            create_order = Order.objects.create(user=self.request.user, seller_id=seller)
            seller_products = [product for product in products if product.user.id == seller]
            create_order.products.set(seller_products)
            create_order.save()

        user = User.objects.get(id=request.user.id)
        serializer = OrderSerializer(user.orders.all(), many=True)

        if len(products) == 0:
            return Response({"message": "Carrinho vazio"})

        user.cart.products_list.clear()
        user.cart.seller_list.clear()

        for product in products:
            product = Product.objects.get(id=product.id)
            if product.stock == 0:
                return Response({"message": f"O produto {product.name} não está disponível "})
            product.stock -= 1

            if product.stock == 0:
                product.status = "indisponivel"
            product.save()
            print(product.stock)


        return Response(serializer.data, status=status.HTTP_201_CREATED)


