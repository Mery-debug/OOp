import pytest
from src.Class_Product import Product


@pytest.fixture()
def product_apple():
    return Product('apple', 'sweet', 129, 15)

