import pytest


@pytest.mark.django_db
def test_ads_get(client, ad):
    expected_response = {
        'Id': ad.pk,
        'name': 'Дрова',
        'author': ad.author_id,
        'price': 2500,
        'description': 'Продаю дрова',
        'is_published': False,
        'category': ad.category_id,
    }

    response = client.get(f"/ads/{ad.pk}", content_type='application/json')

    assert response.status_code == 200
    assert response.data == expected_response
