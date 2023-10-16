import pytest

from selection.models import Selection

# Create your tests here.
@pytest.mark.django_db
def test_selection_creat(client):
    ad = Selection.objects.create(
        name = 'Моя подборка',
        owner = 5,
        items = [4, 7]
    )

    expected_response = {
        "name":'Моя подборка',
        "owner": 5,
        "items": [4, 7]
    }

    response = client.get("/selection/create/")

    assert response.data == expected_response