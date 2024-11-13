from src.Class_Category import Category
from src.Class_Product import Product


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
