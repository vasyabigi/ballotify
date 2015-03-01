from django.db import transaction

from rest_framework import serializers

from questions.models import Question, Choice
from votes.models import Vote
from streams.models import Stream
from .fields import ChoiceRelatedField


class VoteSerializer(serializers.ModelSerializer):
    choice = ChoiceRelatedField(queryset=Choice.objects.all(), slug_field='uuid')
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Vote
        fields = ('choice', 'user_agent', 'ip', 'user')
        read_only_fields = ('user_agent', 'ip', 'user')

    def validate_choice(self, choice):
        if choice.votes.filter(user=self.context['request'].user):
            raise serializers.ValidationError("Already voted. Fuck off!1!!!11")

        return choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('title', 'uuid')
        read_only_fields = ('uuid',)


class QuestionSerializer(serializers.ModelSerializer):
    stream = serializers.SlugRelatedField(queryset=Stream.objects.all(), slug_field='slug')
    slug = serializers.CharField(required=False)
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ('stream', 'title', 'slug', 'choices', 'modified', 'created',)

    @transaction.atomic
    def create(self, validated_data):
        """
        Custom create method. Prepare and create nested choices.

        """
        choices_data = validated_data.pop("choices", None)

        question = Question(**validated_data)
        question.save()

        self.create_choices(question, choices_data)

        return question

    def create_choices(self, question, choices_data):
        Choice.objects.bulk_create(
            [Choice(question=question, **choice_data) for choice_data in choices_data]
        )


class QuestionDetailSerializer(QuestionSerializer):
    class Meta(QuestionSerializer.Meta):
        read_only_fields = ('stream',)
