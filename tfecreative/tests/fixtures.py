import pytest
from tfecreative.core.models import TfeUser


def create_test_user():
    user = TfeUser.objects.create_user(
        username="test_user", email="test_user@tfecreative.com"
    )
    user.set_password("test_user_password123")
    user.save()
    return user


@pytest.fixture()
def test_user():
    return create_test_user()
