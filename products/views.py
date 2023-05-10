from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.permissions import IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema


@extend_schema(tags = ["Product"])
class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = ProductSerializer

    @extend_schema(
            summary = "Product creation"
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    @extend_schema(
            summary = "Product search by name/category/id"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

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

@extend_schema(tags = ["Product"])
@extend_schema(methods = ["PUT"], exclude = True)
class UpdateProduct(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(
            summary = "Product update"
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
