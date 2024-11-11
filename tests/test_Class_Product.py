from src.Class_Product import Product


def test_product_init(product_apple: Product) -> None:
    assert product_apple.name == "apple"
    assert product_apple.description == "sweet"
    assert product_apple.price == 129
    assert product_apple.quantity == 15
