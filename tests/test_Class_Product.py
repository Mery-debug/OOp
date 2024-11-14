from src.Class_Product import Product


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
    assert product4.price == "Цена не должна быть нулевая или отрицательная"


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
