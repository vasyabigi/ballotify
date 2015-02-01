from rest_framework import generics

from accounts.models import User
from .serializers import UserSerializer


class UserDetailView(generics.RetrieveUpdateAPIView):
    """
    Retrieve/Update authenticated user details.

    """
    model = User
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

user_detail_view = UserDetailView.as_view()
