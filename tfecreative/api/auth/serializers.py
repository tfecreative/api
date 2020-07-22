from django.core.validators import RegexValidator
from django.template import Context, Template
from django.template.loader import get_template
from rest_framework import serializers
from tfecreative.core.exceptions import ApiError
from tfecreative.core.mixins import RecaptchaMixin
from tfecreative.core.fields import SanitizedCharField
from tfecreative.services.auth import create_account
from tfecreative.services.email import send_email


class SignInSerializer(serializers.Serializer, RecaptchaMixin):
    recaptcha_code = serializers.CharField(required=True, write_only=True)
    username = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class SignUpSerializer(serializers.Serializer, RecaptchaMixin):
    alphanumeric = RegexValidator(
        r"^[0-9a-zA-Z]*$", "Username contains invalid characters."
    )

    recaptcha_code = serializers.CharField(required=False)
    username = SanitizedCharField(required=True, validators=[alphanumeric])
    email = serializers.EmailField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        email = validated_data.get("email")
        username = validated_data.get("username")
        password1 = validated_data.get("password1")
        password2 = validated_data.get("password2")

        if password1 != password2:
            raise ApiError("Passwords do not match.")

        user = create_account(email, username, password1)

        context = {"username": user.username, "sign_up_url": "https://tfecreative.com"}
        template = get_template("account/email/sign-up-confirmation.html")
        html = template.render(context)

        send_email(recipients=[user.email], subject="Welcome", body=html)
