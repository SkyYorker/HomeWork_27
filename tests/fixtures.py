import pytest

from tests.factories import AdFactory, SelectionFactory


@pytest.fixture
@pytest.mark.django_db
def authorization_token(client, django_user_model):
    username = "test"
    password = "test"

    django_user_model.objects.create_user(
        username=username, password=password, role="moderator", birth_date="1998-06-08")

    response = client.post(
        "/user/token",
        {"username": username, "password": password},
        format="json"
    )

    return response.data['access']


@pytest.fixture
def selection_ads():
    ads = AdFactory.create_batch(2)
    selection = SelectionFactory.create(items=ads)
    return selection
