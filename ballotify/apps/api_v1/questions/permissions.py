from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStreamOwnerOrReadOnly(BasePermission):
    """
    Check if request is safe or authenticated user is owner of question's stream.

    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or view.get_question().stream.owner == request.user


class IsVotedOrPostOnly(BasePermission):
    """
    Check if authenticated user has voted this question.

    """
    def has_permission(self, request, view):
        return request.method not in SAFE_METHODS or view.get_question().votes.filter(user__id=request.user.id).exists()
