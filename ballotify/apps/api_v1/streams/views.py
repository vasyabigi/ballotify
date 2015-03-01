from rest_framework import generics, permissions, response, status, serializers
from rest_framework.settings import api_settings

from streams.models import Stream, StreamMembership
from accounts.models import User
from core.utils import memoized
from ..accounts.serializers import AccountSerializer
from .serializers import StreamSerializer, StreamQuestionSerializer
from .permissions import IsOwnerOrReadOnly


class StreamsView(generics.ListCreateAPIView):
    """
    List/Create streams.

    """
    serializer_class = StreamSerializer

    def get_queryset(self):
        return Stream.objects.public()

    def perform_create(self, serializer):
        serializer.validated_data["owner"] = self.request.user
        serializer.save()

streams_view = StreamsView.as_view()


class StreamMixin(object):
    """
    Share common methods for stream dependent views.

    """
    @memoized
    def get_stream(self):
        return generics.get_object_or_404(Stream, slug=self.kwargs.get("slug"))


class StreamDetailView(StreamMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve/Update/Destroy streams.

    """
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)
    serializer_class = StreamSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Stream.objects.public()

stream_detail_view = StreamDetailView.as_view()


class StreamQuestionsView(StreamMixin, generics.ListAPIView):
    """
    List/Create questions of the specific stream.

    """
    serializer_class = StreamQuestionSerializer

    def get_queryset(self):
        return self.get_stream().questions.all()

    def perform_create(self, serializer):
        serializer.validated_data["stream"] = self.get_stream()
        serializer.save()

stream_questions_view = StreamQuestionsView.as_view()


class StreamQuestionDetailView(StreamMixin, generics.RetrieveAPIView):
    """
    Retrieve/Update/Destroy question of the specific stream.

    """
    serializer_class = StreamQuestionSerializer
    lookup_field = "slug"
    lookup_url_kwarg = "question_slug"

    def get_queryset(self):
        return self.get_stream().questions.all()

stream_question_detail_view = StreamQuestionDetailView.as_view()


class StreamFollowersView(StreamMixin, generics.ListCreateAPIView):
    """
    List followers of `slug` stream. Add new follower by `username` to `slug` stream.

    """
    serializer_class = AccountSerializer

    def get_queryset(self):
        return self.get_stream().followers.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(username=serializer.validated_data["username"])
        if StreamMembership.objects.filter(user=user, stream=self.get_stream()).exists():
            raise serializers.ValidationError({
                api_settings.NON_FIELD_ERRORS_KEY: ["Relationship is already exist."]
            })

        StreamMembership.objects.create(user=user, stream=self.get_stream())
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

stream_followers_view = StreamFollowersView.as_view()


class StreamFollowersView(StreamMixin, generics.ListCreateAPIView):
    """
    List/Create/Delete followers of `slug` stream.

    """
    serializer_class = AccountSerializer

    def get_queryset(self):
        return self.get_stream().followers.all()

    def get_user_and_data(self):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        return User.objects.get(username=serializer.validated_data["username"]), serializer.data

    def create(self, request, *args, **kwargs):
        user, data = self.get_user_and_data()

        if StreamMembership.objects.filter(user=user, stream=self.get_stream()).exists():
            raise serializers.ValidationError({
                api_settings.NON_FIELD_ERRORS_KEY: ["Relationship is already exist."]
            })

        StreamMembership.objects.create(user=user, stream=self.get_stream())
        return response.Response(data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        user, data = self.get_user_and_data()

        if not StreamMembership.objects.filter(user=user, stream=self.get_stream()).exists():
            raise serializers.ValidationError({
                api_settings.NON_FIELD_ERRORS_KEY: ["Relationship does not exist."]
            })

        StreamMembership.objects.get(user=user, stream=self.get_stream()).delete()
        return response.Response(data, status=status.HTTP_204_NO_CONTENT)

stream_followers_view = StreamFollowersView.as_view()
