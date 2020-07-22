import pytest
from django.core.exceptions import ValidationError
from tfecreative.core.exceptions import ApiError
from .auth import create_account


pytestmark = pytest.mark.django_db


def test_create_account():
    user = create_account("test@tfecreative.com", "xtestx", "tfeCreat1v3")
    assert user and user.username == "xtestx"


@pytest.mark.parametrize(
    "password,error", [("123456", "too short"), ("password", "too common!")],
)
def test_create_account_fails_with_invalid_password(password, error):
    with pytest.raises(ValidationError):
        create_account("test@tfecreative.com", "testaccount", password)


def test_create_account_fails_with_unavailable_email():
    create_account("test@tfecreative.com", "test", "tfeCreat1v3")
    with pytest.raises(ApiError):
        create_account("test@tfecreative.com", "test", "tfeCreat1v3")


def test_create_account_fails_with_unavailable_username():
    create_account("test@tfecreative.com", "testxxx", "tfeCreat1v3")
    with pytest.raises(ApiError):
        create_account("test@tfecreative.com", "testxxx", "tfeCreat1v3")
