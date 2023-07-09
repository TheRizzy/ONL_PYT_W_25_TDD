import pytest

from exercises_app.models import Product


@pytest.fixture
def fake_product():
    return Product.objects.create(
        name="fake_name",
        description="fake description",
        price=3,
    )


@pytest.fixture
def tomato_product():
    return Product.objects.create(
        name="tomato",
        description="tomato description",
        price=5
    )


@pytest.fixture
def onion_product():
    return Product.objects.create(
        name="onion",
        description="onion description",
        price=4
    )


@pytest.fixture
def garlic_product():
    return Product.objects.create(
        name="garlic",
        description="garlic description",
        price=3
    )

