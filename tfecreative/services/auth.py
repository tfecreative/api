from django.contrib.auth.password_validation import validate_password
from tfecreative.core.exceptions import ApiError
from tfecreative.core.models import TfeUser, UserProfile


def check_email_availability(email):
    exists = TfeUser.objects.filter(email__iexact=email).exists()
    return not exists


def check_username_availability(username):
    exists = TfeUser.objects.filter(username__iexact=username).exists()
    return not exists


def create_account(email, username, password):
    if not email:
        raise ApiError("Email address is required")

    if not username:
        raise ApiError("Username is required")

    if not password:
        raise ApiError("Password is required")

    if not check_email_availability(email):
        raise ApiError("Email address is already registered")

    if not check_username_availability(email):
        raise ApiError("Username is not available")

    validate_password(password)

    try:
        user = TfeUser.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()

        profile, _ = UserProfile.objects.get_or_create(user=user)
        profile.save()
    except Exception:
        raise ApiError("Failed to create user")
    return user
