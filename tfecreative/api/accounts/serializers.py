from datetime import datetime, timezone
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from tfecreative import settings
from tfecreative.core.mixins import RecaptchaMixin
from tfecreative.core.models import TfeUser


class AccountSerializer(serializers.Serializer):
    class Meta:
        model = TfeUser
        fields = '__all__'

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    username = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.save()
        return instance
