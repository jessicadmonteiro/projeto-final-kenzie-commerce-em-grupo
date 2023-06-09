from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        if request.user.type_user == "vendedor":
            return True
