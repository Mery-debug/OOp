import pytest

from src.Class_Category import Category
from src.Class_Product import Product


@pytest.fixture
def product_apple() -> Product:
    return Product("apple", "sweet", 129, 15)


@pytest.fixture
def category_food() -> Category:
    return Category("food", "some food", ["apple", "banana", "meat", "milk", "eggs"])


@pytest.fixture
def lst_products() -> list:
    return []


@pytest.fixture
def category_magazines() -> Category:
    return Category("magazines", "sth to read", ["magazines", "newspapers", "book"])


@pytest.fixture
def str_exp() -> str:
    return f"Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт.\nXiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
