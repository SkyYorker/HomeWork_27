import pytest


@pytest.mark.django_db
def test_ad_create(client, ad):
    expected_response = {
        "Id": 2,
        "name": 'ДроваДрова',
        "author": ad.author_id,
        "price": 2500,
        "description": 'Продаю дрова',
        "category": ad.category_id,
        "is_published": False
    }

    response = client.post("/ads/create", expected_response)

    assert response.status_code == 201
    assert response.data == expected_response

