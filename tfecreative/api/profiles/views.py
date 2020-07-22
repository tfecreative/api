from django.http import JsonResponse
from rest_framework.views import APIView
from tfecreative.core.exceptions import ApiError
from tfecreative.core.mixins import AuthenticatedMixin
from .serializers import ProfileSerializer
from tfecreative.core import models as core_models


class MyProfileView(AuthenticatedMixin, APIView):
    def get(self, request, uuid=None):
        user = request.user
        user_profile = core_models.UserProfile.objects.get(user=user)
        serializer = ProfileSerializer(user_profile)
        return JsonResponse(data=serializer.data)

    def patch(self, request):
        user = request.user
        user_profile = core_models.UserProfile.objects.get(user=user)
        serializer = ProfileSerializer(
            user_profile,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(data=serializer.data)
