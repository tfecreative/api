from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from tfecreative.core.mixins import AuthenticatedMixin
from . import serializers


class Auth(AuthenticatedMixin, APIView):
    def get(self, request):
        user = request.user
        token = Token.objects.get(user=user)
        return JsonResponse({'token': token.key})


class SignIn(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = serializers.SignInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get('user', None)
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key})


class SignOut(AuthenticatedMixin, APIView):
    def post(self, request):
        response_data = {"message": "You've been signed out."}
        try:
            request.user.auth_token.delete()
            return JsonResponse(response_data, status=200)
        except:
            return JsonResponse(response_data, status=200)


class SignUp(APIView):
    def post(self, request):
        serializer = serializers.SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(data=serializer.data)
