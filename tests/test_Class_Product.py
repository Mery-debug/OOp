import unittest

import pytest

from src.Class_Category import Category
from src.Class_Product import Product, LawnGrass, Smartphone


def test_product_init(product_apple: Product) -> None:
    assert product_apple.name == "apple"
    assert product_apple.description == "sweet"
    assert product_apple.quantity == 15


def test_new_price() -> None:
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    product4.price = 125
    assert product4.price == 125


def test_new_price_1() -> None:
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    product4.price = -1
    assert product4.price == 123000.0


def test_new_product() -> None:
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.quantity == 5


def test_add():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    assert product1 + product2 == 2580000.0
    assert product1 + product3 == 1334000.0
    assert product2 + product3 == 2114000.0


class TestCaseProduct(unittest.TestCase):

    def test_add(self):
        smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                                 "S23 Ultra", 256, "Серый")
        smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
        grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
        grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
        category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
        with self.assertRaises(TypeError):
            invalid_sum = smartphone1 + grass1
            invalid_sum_2 = grass2 + smartphone2
            invalid_sum_3 = grass2 + category_smartphones

    def test_add_positive(self):
        smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                                 "S23 Ultra", 256, "Серый")
        smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
        grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
        grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
        assert grass1 + grass2 == 16750.0
        assert smartphone1 + smartphone2 == 2580000.0

    def test_creation_str(self):
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        assert str(product1) == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт'
        assert str(product2) == 'Iphone 15, 210000.0 руб. Остаток: 8 шт'
        assert str(product3) == 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт'

    def test_repr(self):
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        assert repr(product1) == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    def test_null(self):
        with pytest.raises(ValueError, match='Товар с нулевым количеством не может быть добавлен'):
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)





