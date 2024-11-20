import unittest

from src.Class_Category import Category
from src.Class_Product import Product, Smartphone


def test_category_init(category_food: Category, lst_products: list) -> None:
    assert category_food.name == "food"
    assert category_food.description == "some food"


def test_category_product_count(
    category_magazines: Category, category_food: Category
) -> None:
    assert category_magazines.category_count == 1
    assert category_food.category_count == 1


def test_product_count(category_magazines: Category, category_food: Category) -> None:
    assert category_magazines.product_count == 3
    assert category_food.product_count == 5


def test_category(str_exp) -> None:
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    assert category1.products == str_exp


class TestCase(unittest.TestCase):
    """ Тест класс для обработки выбрасываемой ошибки typeerror """
    def test_add_product(self):
        smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                                 "S23 Ultra", 256, "Серый")
        smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
        category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
        with self.assertRaises(TypeError):
            category_smartphones.add_product("Not a product")


def test_add_category() -> None:
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_smartphones.add_product(smartphone3)
    assert category_smartphones.product_count == 3





