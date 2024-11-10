from src.Class_Category import Category


def test_category_init(category_food: Category, lst_products: list) -> None:
    assert category_food.name == "food"
    assert category_food.description == "some food"
    assert category_food.products == lst_products


def test_category_product_count(category_magazines: Category, category_food: Category) -> None:
    assert category_magazines.category_count == 1
    assert category_food.category_count == 1


def test_product_count(category_magazines: Category, category_food: Category) -> None:
    assert category_magazines.product_count == 3
    assert category_food.product_count == 5
