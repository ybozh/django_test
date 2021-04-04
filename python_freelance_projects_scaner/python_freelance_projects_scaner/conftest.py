import pytest

from python_freelance_projects_scaner.users.models import User
from python_freelance_projects_scaner.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()
