from rest_framework import generics

from .serializers import UserSerializer
from ..streams.serializers import StreamSerializer
from accounts.models import User
from streams.models import Stream


class UserDetailView(generics.RetrieveUpdateAPIView):
    """
    Retrieve/Update authenticated user details.

    """
    model = User
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

user_detail_view = UserDetailView.as_view()


class UserStreamsView(generics.ListCreateAPIView):
    """
    List/Create authenticated user's streams.

    """
    model = Stream
    serializer_class = StreamSerializer

    def get_queryset(self):
        return self.request.user.owned_streams.public()

    def perform_create(self, serializer):
        serializer.validated_data["owner"] = self.request.user
        serializer.save()

user_streams_view = UserStreamsView.as_view()
