from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        owner = getattr(obj, "reported_by")
        return bool(request.user == owner)
