from .models import User
from .serializers import UserSerializer, UserAdmSerializer
from rest_framework.generics import CreateAPIView


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        is_admin = self.request._data["is_admin"]
        serializer.save(is_admin=is_admin)
