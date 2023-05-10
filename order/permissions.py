from rest_framework.permissions import BasePermission


class sellersPermissions(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.type_user == "vendedor":
            return True
