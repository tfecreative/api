from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from tfecreative.core.exceptions import ApiError
from .serializers import StatusSerializer


@authentication_classes([])
@permission_classes([])
class StatusView(APIView):
    def get(self, request):
        serializer = StatusSerializer({})
        return JsonResponse(data=serializer.data)
