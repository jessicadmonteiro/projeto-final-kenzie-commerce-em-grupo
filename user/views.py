from user.permissions import UserAuth
from .models import User
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema

@extend_schema(tags = ["User"])
class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
            summary = "User creation"
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        is_admin = self.request._data["is_admin"]
        serializer.save(is_admin=is_admin)


@extend_schema(tags = ["User"])
@extend_schema(methods = ["PUT"], exclude = True)
class UserViewId(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserAuth]

    @extend_schema(
            summary = "Read user"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
            summary = "User update"
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @extend_schema(
            summary = "Delete user"
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
