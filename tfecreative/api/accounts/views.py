from django.http import JsonResponse
from rest_framework.views import APIView
from tfecreative.core.mixins import AuthenticatedMixin
from . import serializers


class AccountView(AuthenticatedMixin, APIView):
    def get(self, request):
        user = request.user
        serializer = serializers.AccountSerializer(user)
        return JsonResponse(data=serializer.data)

    def patch(self, request):
        user = request.user
        serializer = serializers.AccountSerializer(
            user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(data=serializer.data)
