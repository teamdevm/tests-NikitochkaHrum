import pytest
from django.core.management import call_command
from products.models import Product

@pytest.fixture(scope='function')
def init_data(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock(): 
        call_command('loaddata', "init_data.json") # данные для заполнения лежат в init_data.json