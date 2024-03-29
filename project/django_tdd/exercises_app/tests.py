import pytest
from exercises_app.models import Product


@pytest.mark.django_db
def test_product_detail_view(fake_product, client):
    response = client.get(f'/product/{fake_product.pk}/')
    assert response.status_code == 200
    assert response.context['name'] == fake_product.name
    assert response.context['description'] == fake_product.description
    assert response.context['price'] == fake_product.price


@pytest.mark.django_db
def test_do_not_exists_product_view(client):
    response = client.get("/product/123/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_fail_add_product_view(client):
    response = client.post(
        "/product/add/",
        {
            "name": "Product name",
            "description": "desc",
        }
    )
    assert response.status_code == 200
    assert Product.objects.count() == 0


@pytest.mark.django_db
def test_product_list_view(client, tomato_product, onion_product, garlic_product):
    response = client.get("")
    assert response.status_code == 200
    product_names = []
    for product in response.context['products']:
        product_names.append(product.name)
    assert product_names == [garlic_product.name, onion_product.name, tomato_product.name]
