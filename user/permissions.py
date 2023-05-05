from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework import permissions


class UserAuthenticate(IsAuthenticated, BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class UserAuth(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if obj == request.user:
            return True
        return False
