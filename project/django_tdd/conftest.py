import pytest

from exercises_app.models import Product


@pytest.fixture
def fake_product():
    return Product.objects.create(
        name="fake_name",
        description="fake description",
        price=3,
    )