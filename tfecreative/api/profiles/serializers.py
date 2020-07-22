from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):
    class Meta:
        fields = (
            'uuid',
            'first_name',
            'last_name',
            'email',
            'username',
        )

    uuid = serializers.CharField(read_only=True)
    first_name = serializers.CharField(
        required=False,
        source='user.first_name'
    )
    last_name = serializers.CharField(required=False, source='user.last_name')
    email = serializers.CharField(required=False, source='user.email')
    username = serializers.CharField(required=False, source='user.username')

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        user = instance.user
        user.first_name = validated_data.get('first_name', user.first_name)
        user.last_name = validated_data.get('last_name', user.last_name)
        user.save()
        return user
