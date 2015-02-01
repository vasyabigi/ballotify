from accounts.models import User

from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'name', 'link',)
        read_only_fields = ('name', 'link',)

    def validate_username(self, username):
        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError("User does not exist.")

        return username
