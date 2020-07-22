import pytest
from tfecreative.tests.fixtures import test_user


@pytest.mark.django_db
def test_create_user_fixture(test_user):
    user = test_user
    assert user.username
