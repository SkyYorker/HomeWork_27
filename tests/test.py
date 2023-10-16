
import pytest

from ads.models import Ad
from user.models import User
from cat.models import Category

@pytest.mark.django_db
def test_ad_create(client):
    user = User.objects.create_user(
        username = "skyyorke",
        password = "12345",
        birth_date = "1998-06-08",
        email = "mail@.ru"
    )
    category = Category.objects.create(
        name = 'Дровишки',
        slug = 'Д'
    )
    ad = Ad.objects.create(
        name='Дрова',
        author=user,
        price=2500,
        description='Продаю дрова',
        category=category,
    )

    expected_response = {
        "Id": ad.pk,
        "name": 'Дрова',
        "author_id": user.id,
        "price": 2500,
        "description": 'Продаю дрова',
        "category_id": category.id
    }

    response = client.post("/ads/create")
    
    assert response.conten_type == "application/json"
    assert response.status_code == 200
    assert response.data == expected_response
    



