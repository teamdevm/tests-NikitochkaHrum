import pytest
from products.models import Product

@pytest.mark.django_db
def test_product_creation():
       product = Product.objects.create(
           name='T-Shirt',
           price=19.99,
           description='Comfortable cotton t-shirt',
           category='Tops',
           image='./static/product_images/placeholder.png'
       )
       
       assert product.name == 'T-Shirt'
       assert product.price == 19.99
       assert product.description == 'Comfortable cotton t-shirt'
       assert product.category == 'Tops'