from questions.models import Question

from rest_framework import serializers

from streams.models import Stream


class QuestionSerializer(serializers.ModelSerializer):
    stream = serializers.SlugRelatedField(queryset=Stream.objects.all(), slug_field='slug')
    slug = serializers.CharField(required=False)

    class Meta:
        model = Question
        fields = ('stream', 'title', 'slug', 'modified', 'created',)


class QuestionDetailSerializer(QuestionSerializer):
    class Meta(QuestionSerializer.Meta):
        read_only_fields = ('stream',)
