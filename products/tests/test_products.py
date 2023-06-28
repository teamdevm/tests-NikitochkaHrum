from products.models import Product
import pytest

@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(name='New Product', price=9.99, description='Test product', category='Test Category')
    assert product.id is not None
    assert product.name == 'New Product'
    assert product.price == 9.99
    assert product.description == 'Test product'
    assert product.category == 'Test Category'