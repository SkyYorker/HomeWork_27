import factory

from ads.models import Ad
from user.models import User
from cat.models import Category
from selection.models import Selection


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "12345"
    birth_date = "1998-06-08"
    email = factory.Faker("email")


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category

    name = 'Дровишки'
    slug = factory.Faker("slug")


class AdFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Ad


    name = 'Дрова'
    author = factory.SubFactory(UserFactory)
    price = 2500
    description = 'Продаю дрова'
    category = factory.SubFactory(CategoryFactory)


class SelectionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Selection

    name = 'Моя подборка',
    owner = factory.SubFactory(UserFactory)
    @factory.post_generation
    def items(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.items.set(extracted)

    # items = factory.SubFactory(AdFactory)