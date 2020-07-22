from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from tfecreative import settings
from tfecreative.core.exceptions import ApiError
import requests


class AuthenticatedMixin:
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class RecaptchaMixin:
    validated_data: None

    def validate_recaptcha_code(self, recaptcha_code):
        if settings.DEBUG or not settings.RECAPTCHA_ENABLED:
            return True

        valid = self.check_recaptcha(value=recaptcha_code)
        if not valid:
            raise ApiError('Invalid recaptcha code')
        return True

    def check_recaptcha(self, value=None):
        try:
            if not value:
                recaptcha_code = self.validated_data.get(
                    'recaptcha_code', None)
            else:
                recaptcha_code = value
            response_json = self.verify_recaptcha_code(recaptcha_code)
            return response_json['success'] is True
        except (ValueError, requests.exceptions.RequestException):
            return False

    def verify_recaptcha_code(self, recaptcha_code):
        post_data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recaptcha_code
        }
        r = requests.post(settings.RECAPTCHA_VERIFICATION_URL, post_data)
        return r.json()
