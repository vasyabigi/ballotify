from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStreamOwnerOrReadOnly(BasePermission):
    """
    Check if request is safe or authenticated user is owner of question's stream.

    """
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or view.get_question().stream.owner == request.user
