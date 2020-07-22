from rest_framework import serializers
from tfecreative import settings
from tfecreative.core.exceptions import ApiError


class StatusSerializer(serializers.Serializer):
    status = serializers.SerializerMethodField()
    environment = serializers.SerializerMethodField()

    def get_environment(self, obj):
        return settings.ENVIRONMENT_NAME

    def get_status(self, obj):
        return 'Running'

    def create(self, validated_data):
        raise ApiError()

    def update(self, instance, validated_data):
        raise ApiError()
