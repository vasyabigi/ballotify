from rest_framework import generics, permissions

from questions.models import Question
from core.utils import memoized
from .serializers import QuestionSerializer, QuestionDetailSerializer, ChoiceSerializer, VoteSerializer
from .permissions import IsStreamOwnerOrReadOnly, IsVotedOrPostOnly
from .utils import get_client_ip


class QuestionsView(generics.ListCreateAPIView):
    """
    List/Create questions.

    """
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()

questions_view = QuestionsView.as_view()


class QuestionMixin(object):
    """
    Share common methods for stream dependent views.

    """
    @memoized
    def get_question(self):
        return generics.get_object_or_404(Question, slug=self.kwargs.get("slug"))


class QuestionDetailView(QuestionMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve/Update/Destroy question.

    """
    permission_classes = (permissions.IsAuthenticated, IsStreamOwnerOrReadOnly,)
    serializer_class = QuestionDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Question.objects.all()

question_detail_view = QuestionDetailView.as_view()


class ChoicesView(QuestionMixin, generics.ListCreateAPIView):
    """
    List/Create choices for specific question.

    """
    permission_classes = (permissions.IsAuthenticated, IsStreamOwnerOrReadOnly,)
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        return self.get_question().choices.all()

    def perform_create(self, serializer):
        serializer.validated_data["question"] = self.get_question()
        serializer.save()

choices_view = ChoicesView.as_view()


class VotesView(QuestionMixin, generics.ListCreateAPIView):
    """
    List/Create votes for specific question.

    """
    permission_classes = (permissions.IsAuthenticated, IsVotedOrPostOnly,)
    serializer_class = VoteSerializer

    def get_queryset(self):
        return self.get_question().votes.all()

    def perform_create(self, serializer):
        serializer.validated_data.update({
            "user": self.request.user,
            "question": self.get_question(),
            "ip": get_client_ip(self.request),
            "user_agent": self.request.META.get('HTTP_USER_AGENT')
        })

        serializer.save()

votes_view = VotesView.as_view()
