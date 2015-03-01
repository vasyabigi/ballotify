from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Check if request is safe or authenticated user is owner.

    """
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or view.get_stream().owner == request.user
