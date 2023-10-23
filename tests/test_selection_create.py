import pytest

from ads.Serializer import AdSerializer
from tests.fixtures import authorization_token

@pytest.mark.django_db
def test_selection_create(client, user, authorization_token, selection_ads):
    expected_response = {
        "id": 2,
        "name": 'Моя подборка',
        "owner": user.id,
        "items": list(selection_ads.items.values_list('Id', flat=True))
    }

    response = client.post("/selection/create/", expected_response, HTTP_AUTHORIZATION="Bearer " + authorization_token)

    assert response.data == expected_response
    assert response.status_code == 201

