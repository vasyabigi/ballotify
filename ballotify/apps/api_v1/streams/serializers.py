from streams.models import Stream

from rest_framework import serializers

from ..questions.serializers import QuestionSerializer


class StreamSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(required=False)

    class Meta:
        model = Stream
        fields = ('title', 'slug', 'modified', 'created',)


class StreamQuestionSerializer(QuestionSerializer):
    class Meta(QuestionSerializer.Meta):
        fields = ('title', 'slug', 'choices', 'modified', 'created',)
