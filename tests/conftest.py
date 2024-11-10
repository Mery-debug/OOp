import pytest

from src.Class_Category import Category
from src.Class_Product import Product


@pytest.fixture()
def product_apple() -> Product:
    return Product("apple", "sweet", 129, 15)


@pytest.fixture()
def category_food() -> Category:
    return Category("food", "some food", ["apple", "banana", "meat", "milk", "eggs"])


@pytest.fixture()
def lst_products() -> list:
    return ["apple", "banana", "meat", "milk", "eggs"]


@pytest.fixture()
def category_magazines() -> Category:
    return Category("magazines", "sth to read", ["magazines", "newspapers", "book"])
