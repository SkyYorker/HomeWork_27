import pytest

from tests.fixtures import authorization_token


@pytest.mark.django_db
def test_ads_get(client, authorization_token, ad):
    expected_response = {
        'count': 1,
        'next': None,
        'previous': None,
        'results': [
            {
                'Id': ad.pk,
                'name': 'Дрова',
                'author': ad.author_id,
                'price': 2500,
                'description': 'Продаю дрова',
                'is_published': False,
                'category': ad.category_id,
            }
        ]

    }

    response = client.get("/ads/", content_type='application/json',
                          HTTP_AUTHORIZATION="Bearer " + authorization_token)

    assert response.status_code == 200
    assert response.data == expected_response


