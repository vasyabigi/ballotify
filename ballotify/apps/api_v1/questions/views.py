from rest_framework import generics, permissions

from questions.models import Question
from core.utils import memoized
from .serializers import QuestionSerializer, QuestionDetailSerializer
from .permissions import IsStreamOwnerOrReadOnly


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
    def get_stream(self):
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
