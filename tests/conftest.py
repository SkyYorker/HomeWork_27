from pytest_factoryboy import register
from tests.factories import UserFactory, CategoryFactory, AdFactory, SelectionFactory

register(UserFactory)
register(CategoryFactory)
register(AdFactory)
register(SelectionFactory)

pytest_plugins = "tests.fixtures"
