from streams.models import Stream

from rest_framework import serializers


class StreamSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(required=False)

    class Meta:
        model = Stream
        fields = ('title', 'slug', 'modified', 'created',)
