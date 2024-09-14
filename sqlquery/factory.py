import factory
from factory.faker import faker

from .models import Product

FAKE = faker.Faker()


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("sentence", nb_words=12)
    slug = factory.Faker("slug")
    is_digital = False
